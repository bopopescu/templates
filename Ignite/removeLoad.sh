#!/bin/bash

ssh -p 50000 negat@51.141.13.25 'kill $(pgrep -f apply)'
ssh -p 50001 negat@51.141.13.25 'kill $(pgrep -f apply)'


