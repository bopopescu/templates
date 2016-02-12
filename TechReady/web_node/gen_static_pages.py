################################################################################
#
# helper functions for generating static web pages for nginx to serve
# that will show the original and stitched-together image
#

def cat():
    ret = '''
<!DOCTYPE html>
<html>
  <head>
    <title>Photo Mosaic</title>
<script src="https://code.jquery.com/jquery-2.2.0.js" crossorigin="anonymous"></script>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>


  </head>
  <body>
<div class="container" id="helperMain" style="white-space: nowrap;">
    '''
    row_len = 30
    for row_index in range(0, row_len):
        ret += '<div class="row">'
        for column_index in range(0, row_len):
            ret += '<img height="32" width="32" src="/orangeCat960/decomposed_cat_face_' + str(row_index) + '_' + str(column_index) + '.png">'

        ret += '</div>'
    ret += '''
    </div>
    </body>
    </html>
    
    '''

    return ret



def cat_substitute():
    ret = '''
<!DOCTYPE html>
<html>
  <head>
    <title>Photo Mosaic</title>
<script src="https://code.jquery.com/jquery-2.2.0.js" crossorigin="anonymous"></script>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>


  </head>
  <body>
<div class="container" id="helperMain" style="white-space: nowrap;">
    '''
    row_len = 30
    for row_index in range(0, row_len):
        ret += '<div class="row">'
        for column_index in range(0, row_len):
            ret += '<img height="32" width="32" src="/decomposed_cat_face_substitute_' + str(row_index) + '_' + str(column_index) + '.png">'

        ret += '</div>'
    ret += '''
    </div>
    </body>
    </html>
    
    '''

    return ret

#print(cat())
#print(cat_substitute())
