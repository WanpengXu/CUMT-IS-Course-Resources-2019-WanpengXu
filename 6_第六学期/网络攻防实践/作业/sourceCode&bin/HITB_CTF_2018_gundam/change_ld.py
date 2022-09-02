#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
import argparse
import os

fail = log.failure

def check_args(args):
    if not args.binary:
        fail("No binary filename given")
        sys.exit(-1)
    else:
        if not os.path.isfile(args.binary):
            fail("Binary file {} doesn't exist".format(args.binary))
            sys.exit(-1)

    if not args.ld:
        fail("No ld.so filename given")
        sys.exit(-1)
    else:
        if not os.path.isfile(args.ld):
            fail("ld file {} doesn't exist".format(args.ld))
            sys.exit(-1)
    
    if not args.output:
        fail("No output filename given")
        sys.exit(-1)
    else:
        if os.access(args.output, os.F_OK): 
            os.remove(args.output)
            info("Removing exist file {}".format(args.output))

def changeld(binary, ld, output):
    """
    assign new ld.so by changing the binary
    """
    binary = ELF(binary)
    for segment in binary.segments:
        if segment.header['p_type'] == 'PT_INTERP':
            size = segment.header['p_memsz']
            addr = segment.header['p_paddr']
            data = segment.data()
            if size <= len(ld):
                fail("Failed to change PT_INTERP from {} to {} (ld.so path name too long)".format(data, ld))
                return None
            binary.write(addr, ld.ljust(size, '\0'))
            binary.save(output)    
            os.chmod(output, 0b111000000) #rwx------
    log.success("PT_INTERP has changed from {} to {}. Save to {}".format(data, ld, output)) 

parser = argparse.ArgumentParser(description='Simple utility to assign new ld.so of the given binary')
parser.add_argument('-b', '--binary', action='store', dest="binary", help='Filename of the input binary')
parser.add_argument('-l', '--ld', action='store', dest="ld", help='Filename of the ld.so')
parser.add_argument('-o', '--output',action='store', dest="output", help='Output file')
args = parser.parse_args()
check_args(args)

changeld(args.binary, args.ld, args.output)
