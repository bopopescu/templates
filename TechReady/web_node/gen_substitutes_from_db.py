#import math
#import png
#import cPickle
#import timeit
#import numpy as np
#import sys
import subprocess
import time
import mysql.connector
from credentials import *

#from get_work import *


'''
fo1 = open('cifar-10-batches-py/data_batch_1', 'rb')
dict1 = cPickle.load(fo1)
fo1.close()
fo2 = open('cifar-10-batches-py/data_batch_2', 'rb')
dict2 = cPickle.load(fo2)
fo2.close()
fo3 = open('cifar-10-batches-py/data_batch_3', 'rb')
dict3 = cPickle.load(fo3)
fo3.close()
fo4 = open('cifar-10-batches-py/data_batch_4', 'rb')
dict4 = cPickle.load(fo4)
fo4.close()
fo5 = open('cifar-10-batches-py/data_batch_5', 'rb')
dict5 = cPickle.load(fo5)
fo5.close()
'''
#dict = {'data': np.append([], [dict1['data']])}#, dict2['data'], dict3['data'], dict4['data'], dict5['data']])}


#fo = open('cifar-10-batches-py/data_batch_1', 'rb')
#dict = cPickle.load(fo)
#fo.close()

#pic_side_len = 32
#num_pics = len(dict['data'])


def row_to_triplet(pic_row):
    num_pixels = pic_side_len * pic_side_len
    red = pic_row[:num_pixels]
    green = pic_row[num_pixels:2*num_pixels]
    blue = pic_row[2*num_pixels:]
    out = []
    for row_index in range(pic_side_len):
        row = []
        for column_index in range(pic_side_len):
            color_index = row_index*pic_side_len + column_index
            row.append(red[color_index])
            row.append(green[color_index])
            row.append(blue[color_index])
            
        out.append(row)

    return out

def quad_to_row(quad):
    red = np.array([])
    green = np.array([])
    blue = np.array([])
    for row in quad:
        row_len = len(row)
        for column_index in range(0, row_len):
            if column_index % 4 == 0:
                red = np.append(red, row[column_index])
            elif column_index % 4 == 1:
                green = np.append(green, row[column_index])
            elif column_index % 4 == 2:
                blue = np.append(blue, row[column_index])


    pic_row = np.append([], [red, green, blue])
    return pic_row

def triplet_to_row(triplet):
    red = np.array([])
    green = np.array([])
    blue = np.array([])
    for row in triplet:
        row_len = len(row)
        for column_index in range(0, row_len):
            if column_index % 3 == 0:
                red = np.append(red, row[column_index])
            elif column_index % 3 == 1:
                green = np.append(green, row[column_index])
            elif column_index % 3 == 2:
                blue = np.append(blue, row[column_index])


    pic_row = np.append([], [red, green, blue])
    return pic_row

def parse_row_pic_from_file(file_name):
    r=png.Reader(file=open(file_name, 'rb'))
    pic_ds = r.read()
    ret = quad_to_row(pic_ds[2])
    return ret

def parse_row_pic_from_file_triplet(file_name):
    r=png.Reader(file=open(file_name, 'rb'))
    pic_ds = r.read()
    ret = triplet_to_row(pic_ds[2])
    return ret

def write_row_pic_to_file(row_pic, file_name):
    out = row_to_triplet(row_pic)
    f = open(file_name, 'wb')
    w = png.Writer(pic_side_len, pic_side_len)
    w.write(f, out)

def ssqd(target_row, candidate_row):
    target_row = target_row.astype(np.int32)
    candidate_row = candidate_row.astype(np.int32)
    diffs = target_row - candidate_row
    square_diffs = diffs*diffs
    ret = sum(square_diffs)
    return ret

def index_of_best_match(target_row):
    min_val = 10000000000
    min_index = -1
    for index in range(0, num_pics):
        err = ssqd(target_row, dict['data'][index])
        if (err < min_val):
            min_val = err
            min_index = index

    return min_index

# large_row_pic must by (pic_side_len*n) by (pic_side_len*n) for n > 0
# returns dict s.t. dict[row_chunk_index][column_chunk_index] = small_row_pic
def decompose_large_row_pic(large_row_pic):
    large_row_pic_len = len(large_row_pic)
    large_row_num_pixels = large_row_pic_len/3
    large_row_pic_side_len = int(math.sqrt(large_row_num_pixels))
    print(large_row_pic_side_len)
    assert (large_row_pic_side_len % pic_side_len == 0)
    side_factor = large_row_pic_side_len / pic_side_len
    large_row_pic_red = np.array(large_row_pic[:large_row_num_pixels])
    large_row_pic_green = np.array(large_row_pic[large_row_num_pixels:2*large_row_num_pixels])
    large_row_pic_blue = np.array(large_row_pic[2*large_row_num_pixels:])

    ret = {}
    for row_chunk_index in range(0, side_factor):
        for column_chunk_index in range(0, side_factor):
            cur_red = np.array([])
            cur_green = np.array([])
            cur_blue = np.array([])
            for small_row_index in range(0, pic_side_len):
                starting_index = row_chunk_index*large_row_pic_side_len*pic_side_len + column_chunk_index*pic_side_len + small_row_index*large_row_pic_side_len
                for pixel_index in range(0, pic_side_len):
                    cur_red = np.append(cur_red, large_row_pic_red[starting_index + pixel_index])
                    cur_green = np.append(cur_green, large_row_pic_green[starting_index + pixel_index])
                    cur_blue = np.append(cur_blue, large_row_pic_blue[starting_index + pixel_index])

            if row_chunk_index not in ret:
                ret[row_chunk_index] = {}

            ret[row_chunk_index][column_chunk_index] = np.append([], [cur_red, cur_green, cur_blue])
                
            
    return ret

'''
def gen_cat(filename):
    print('parsing pic')
    cat_face = parse_row_pic_from_file(filename)
    print('decomposing pic')
    decomposed_cat_face = decompose_large_row_pic(cat_face)
    for row_chunk_index in decomposed_cat_face:
        for column_chunk_index in decomposed_cat_face[row_chunk_index]:
            print ('row: ' + str(row_chunk_index) + ', column: ' + str(column_chunk_index))
            row_pic = decomposed_cat_face[row_chunk_index][column_chunk_index]
            best_matching_index = index_of_best_match(row_pic)
            write_row_pic_to_file(dict['data'][best_matching_index], 'static/decomposed_cat_face_substitute_' + str(row_chunk_index) + '_' + str(column_chunk_index) + '.png')
            write_row_pic_to_file(row_pic, 'static/decomposed_cat_face_' + str(row_chunk_index) + '_' + str(column_chunk_index) + '.png')
'''

def gen_decomposed(filename):
    print('parsing pic')
    #cat_face = parse_row_pic_from_file(filename)
    cat_face = parse_row_pic_from_file_triplet(filename)
    print('decomposing pic')
    decomposed_cat_face = decompose_large_row_pic(cat_face)
    for row_chunk_index in decomposed_cat_face:
        for column_chunk_index in decomposed_cat_face[row_chunk_index]:
            print ('row: ' + str(row_chunk_index) + ', column: ' + str(column_chunk_index))
            row_pic = decomposed_cat_face[row_chunk_index][column_chunk_index]
            write_row_pic_to_file(row_pic, 'orangeCat960/decomposed_cat_face_' + str(row_chunk_index) + '_' + str(column_chunk_index) + '.png')

def gen_substitute(decomposed_cat_face):
    print('generating substitute')
    for row_chunk_index in decomposed_cat_face:
        for column_chunk_index in decomposed_cat_face[row_chunk_index]:
            print ('  row: ' + str(row_chunk_index) + ', column: ' + str(column_chunk_index))
            row_pic = decomposed_cat_face[row_chunk_index][column_chunk_index]
            best_matching_index = index_of_best_match(row_pic)
            write_row_pic_to_file(dict['data'][best_matching_index], 'static/decomposed_cat_face_substitute_' + str(row_chunk_index) + '_' + str(column_chunk_index) + '.png')
            write_row_pic_to_file(row_pic, 'static/decomposed_cat_face_' + str(row_chunk_index) + '_' + str(column_chunk_index) + '.png')

def compose_from_pieces(fileprefix, n):
    print('composing')
    composition = {}
    for row_index in range(0, n):
        composition[row_index] = {}
        for column_index in range(0, n):
            print('  row: ' + str(row_index) + ', column: ' + str(column_index))
            composition[row_index][column_index] = parse_row_pic_from_file_triplet(fileprefix + '_' + str(row_index) + '_' + str(column_index) + '.png')

    return composition


'''
def sample_work():
    composition = compose_from_pieces('static/orangeCat960/decomposed_cat_face', 30)
    gen_substitute(composition)

def grump64():
    parse_row_pic_from_file('grumpyCat64.png')
def grump128():
    parse_row_pic_from_file('grumpyCat128.png')
def grump192():
    parse_row_pic_from_file('grumpyCat192.png')
def cf():
    parse_row_pic_from_file('cat_face.png')
def grump640():
    parse_row_pic_from_file('grumpyCat.png')
'''

#gen_decomposed('mona.png')

#print(timeit.timeit(work, number=1))

'''
while True:
    print('getting work')
    sys.stdout.flush()
    work_to_do = get_work()
    if len(work_to_do) == 0:
        break

    for tup in work_to_do:
        row_index = tup[0]
        column_index = tup[1]
        print('  row: ' + str(row_index) + ', column: ' + str(column_index))
        sys.stdout.flush()
        fname = 'static/orangeCat960/decomposed_cat_face_' + str(row_index) + '_' + str(column_index) + '.png'
        row_pic = parse_row_pic_from_file_triplet(fname)
        best_matching_index = index_of_best_match(row_pic)
        write_row_pic_to_file(dict['data'][best_matching_index], 'static/decomposed_cat_face_substitute_' + str(row_index) + '_' + str(column_index) + '.png')
 '''
def gen_substitutes_from_db():
    cnx = mysql.connector.connect(user=username, password=password, host=hostname, database='trvmssdb')
    cnx.start_transaction(isolation_level='SERIALIZABLE')
    cursor = cnx.cursor()
    
    select_query = '''
    SELECT * FROM work WHERE status="done";
    '''
    
    cursor.execute(select_query)
    ret = []
    for row in cursor:
        best_matching_index = row[3]
        com = ['cp', 'static/' + str(best_matching_index) + '.png', 'static/decomposed_cat_face_substitute_' + str(row[0]) + '_' + str(row[1]) + '.png']
        #print(com)
        subprocess.Popen(com)
        
        
    cnx.commit()
    cursor.close()
    cnx.close()

    return ret


while True:
    gen_substitutes_from_db()
    time.sleep(15)

