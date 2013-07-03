#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id: commit_new_description.py 383 2009-08-20 17:07:55Z oneliner $
# $HeadURL: https://svn.blender.org/svnroot/bf-extensions/contrib/dev-tools/flatten_svn.py $
# --------------------------------------------------------------------------
# commit_new_description.py
# Copyright Carlos Santana 2010
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------
'''

-Usage

-- for c comments (ot->description)
--- commit_new_c_desc
takes two parameters


param 1: dictionary in {"ot->idname":"comment","ot->idname#":"comment#"} format

    considerations: comment should be clear of starting and trailing "triple single quotes" and quotes must be escaped(\" \')

    also comment MUST be single line, else the parsing will fail to recognize end of comment and result in a corrupted file

param 2:[optional] directory root for start of recursiveness (if not present will start recursiveness from current working directory)


---return

nothing

-- for py scripts (comment line below class definition)
--- commit_new_py_desc
takes two parameters

param 1: dictionary in {"bl_idname":"comment","bl_idname#":"comment#"} format

    considerations: comment should be clear of starting and trailing "triple single quotes" and quotes must be escaped(\" \')

    also comment MUST be single line, else the parsing will fail to recognize end of comment and result in a corrupted file

param 2:[optional] directory root for start of recursiveness (if not present will start recursiveness from current working directory)

---invoke examples

2params
commit_new_py_desc({"mesh.primitive_torus_add":"Add a \"torus mesh\", yeah, those doughnut looking things","bl_idname_N":"desc_N"}, "C:\\BlenderSVN\\blender\\release\\scripts")

1param
commit_new_py_desc({"mesh.primitive_torus_add":"Add a \"torus mesh\", yeah, those doughnut looking things","bl_idname_N":"desc_N"})


---return

nothing

-- for op descriptions
--- commit_new_op_desc
takes two parameters

param 1: dictionary in {{"ClassName": [["PropertyType","NameAttributeValueOfPropertyType","Description"],["PropertyType_N","NameAttributeValueOfPropertyType_N","Description_N"]],
                          "ClassName_N": [["PropertyType_NN","NameAttributeValueOfPropertyType_NN","Description_NN"],["PropertyType_N_NN","NameAttributeValueOfPropertyType_N_NN","Description_N_NN"]],          } format

    considerations: comment should be clear of starting and trailing "triple single quotes" and quotes must be escaped(\" \')

    also comment MUST be single line, else the parsing will fail to recognize end of comment and result in a corrupted file

    if only one list is provided for any given classname entry,.. it must be wraped inside a container list
    
param 2:[optional] directory root for start of recursiveness (if not present will start recursiveness from current working directory)

---invoke example
commit_new_op_desc({"AddGear": [["IntProperty","Number of Teeth","Number of teeth on the gear(altered)"],
                                ["FloatProperty","Radius","Radius of the gear, negative for crown gear(altered)"],
                                ["FloatProperty","Conical angle", "Conical angle of gear (degrees)(altered)" ]
                                ],
                    "AddGem":[["IntProperty","Segments","Longitudial segmentation(altered)"],
                              ["FloatProperty","Table height","Height of the top half.(altered)"]
                              ],
                    "PropertyPanel":[["FloatProperty", "Min", "Minimum ammount of whatever is beeing used(altered)"]],
                    "VertexPaintDirt":[["FloatProperty", "Blur Strength", "Blur strength per iteration(altered)" ],
                                       ["IntProperty", "Blur Iterations", "Number times to blur the colors. (higher blurs more)(altered)"]]
                    },
                   
                   "C:\\blender_py\\release")
'''
import os 

import re


def find_start_idname( file_content, start_index, start_type):
    ''' finding where idname block starts helps find (or declare non existent) comment in code blocks'''
    line_counter = start_index -1
    while True:
        if file_content[line_counter].startswith(start_type):
            return line_counter
        if line_counter <1:
            return False
        line_counter -=1

    
def get_filelist_rec(file_ext, use_dir):
    '''recursive directory tree lookup according to file extension'''
    foundfiles = []
    '''print "using dictionary provided: ", bl_desc_pairs'''
    if use_dir=="local":
        '''print "using default relative path"'''
        cur_wrk_dir= os.getcwd()    
    else:
        cur_wrk_dir=use_dir
        '''print "using supplied path: ", cur_wrk_dir'''
    for root,dir,files in os.walk(cur_wrk_dir):
   
        filelist = [ os.path.join(root,fi) for fi in files if fi.endswith(file_ext) ]
   
        for f in filelist:
  
            foundfiles.append(f)
    if len(foundfiles)>0:
        return foundfiles
    else:
        return -1
def commit_new_rna_desc(rna_desc_pairs, use_dir="local"):
    print "this one got me woopped for now"


def commit_new_c_desc(ot_desc_pairs,use_dir="local"):




    allfiles = []

    allfiles = get_filelist_rec(".c", use_dir)
  
    if allfiles > 0: 
        for i in allfiles:
            print i
            f= open(i)
            f_content= f.readlines()
            f.close()
            '''print "there are " , len(f_content), "lines in the file",i'''
            found_idname = 0
            line_record = 0
            action = ""
            overwrite = False
            add_lines_task= False
            add_lines = []
            add_lines_at=[]
            add_lines_offset = 0
            for lines in f_content:
                search_term = "ot->idname ="
                if lines.find(search_term)>0:
                    '''print "\n found  ", search_term ," at line", line_record'''
                    found_idname = line_record
                    clean_ot_idname= re.search('\s+ot->idname\s*=\s*["\']*([^"\';]+)["\']*', f_content[line_record])
                    if clean_ot_idname:
                        '''print "value :", clean_ot_idname.group(1)'''
                        if ot_desc_pairs.has_key(clean_ot_idname.group(1)) :
                            overwrite = True
                            
                            found_void=find_start_idname( f_content, line_record, "void")
                            if found_void:
                                
                                ot_new_description="        ot->description = \""+ot_desc_pairs[clean_ot_idname.group(1)]+"\"; \n"
                                while(found_void < len(f_content)):
                                    found_end = re.search('^\}[^,;]\s*$', f_content[found_void])
                                    found_description = re.search('ot->description\s*=\s*["\'](.*)["\']',f_content[found_void])
                                    if found_description:
                                        '''print "found description ", f_content[found_void], " for idname found at line ", found_idname'''
                                        '''print "value ", found_description.group(1)'''
                                        f_content[found_void] = ot_new_description
                                        break
                                    if found_end:
                                        '''print "found void at " , found_void'''
                                        '''print " entry has no description for idname found at ", found_idname'''
                                        add_lines_task = True
                                        add_lines.append(ot_new_description)
                                        add_lines_at.append(found_idname)
                                        break
                                    '''print "line_record " , line_record'''
                                    
                                        
                                    found_void += 1
                                
                        else:
                             '''print "not in dictionary list "'''
                line_record += 1
            if overwrite:
                
                if add_lines_task:
                    '''f_content.insert(index , new_comment)'''
                    for newline in add_lines:
                        index= add_lines_at[add_lines_offset]+ add_lines_offset
                        f_content.insert(index, newline)
                        add_lines_offset += 1
                '''print "the file ", i , "will be OVERWRITTEN, god help us all"'''
                outf = open(i, 'w')
                for outl in f_content:
                    outf.write(outl)
                outf.close()
                
def commit_new_py_desc(bl_desc_pairs, use_dir="local"): 
    
    '''print "starting function (imported os, re)"'''

    
    allfiles = []

    allfiles = get_filelist_rec(".py", use_dir)
  
    if allfiles > 0: 
        for i in allfiles:
      
            print "file ", i
            f= open(i)
            f_content= f.readlines()
            f.close()
            '''print "there are " , len(f_content), "lines in the file",i'''
            line_record = 0
            action = ""
            overwrite = False
            for lines in f_content:
                search_term = "bl_idname ="
                if lines.find(search_term)>0:
                    print "\n found  ", search_term ," at line", line_record
                    clean_bl_idname= re.search('bl_idname\s*=\s*["\']([^"\']+)["\']', f_content[line_record])
                    if clean_bl_idname:
                        print "value :", clean_bl_idname.group(1)
                        found_class=find_start_idname( f_content, line_record, "class")
                        if found_class:
                            found_comment= re.search('^\s+[\'"\#]+([^\'"]+)', f_content[found_class +1])
                            
                            if found_comment:
                                action = "edit"
                                '''print "current comment: ", found_comment.group(1), "\n"'''
                                '''print "from original", f_content[found_class +1]'''
                            else:
                                '''print "didint find a current comment\n"'''
                                action = "add new"
                                
                        
                        
                        if bl_desc_pairs.has_key(clean_bl_idname.group(1)) :
                            overwrite = True
                            index = found_class +1
                            new_comment = "    '''" + bl_desc_pairs[clean_bl_idname.group(1)] + "''' \n"
                            '''print "\n\n\n This entry is meant for correction"
                            print "will ", action, " with value: ",  bl_desc_pairs[clean_bl_idname.group(1)], "\n\n\n"'''
                            if action == "edit":
                                f_content[index]=new_comment
                            else:
                                
                                f_content.insert(index , new_comment)
                                line_record +=1
                line_record +=1
            if overwrite:
                print "the file ", i , "will be OVERWRITTEN, god help us all"
                outf = open(i, 'w')
                for outl in f_content:
                    outf.write(outl)
                outf.close()
    else:
        print "didint find any files to look at"

def commit_new_op_desc(op_desc_pairs, use_dir="local"):
    allfiles = []

    allfiles = get_filelist_rec(".py", use_dir)
    
    
    if allfiles > 0:
        for i in allfiles:
            all_classes = {}
            '''print i'''
            f= open(i)
            f_content= f.readlines()
            f.close()
            for ln, lines in enumerate(f_content):
                found_class= re.search('^class\s+([^\(]+)',lines)
                if found_class and op_desc_pairs.has_key(found_class.group(1)):
                    print i
                    '''print found_class.group(1)'''
                    print "\n\n", lines, " at ", ln
                    print len(op_desc_pairs[found_class.group(1)])
                    for j_ln, jobs in enumerate(op_desc_pairs[found_class.group(1)]):
                        '''print "pending ", j_ln , jobs'''
                        print op_desc_pairs[found_class.group(1)][j_ln][0]
                        
                        job_ln= ln + 1
                        job_regex= "^\s*\w+\s*=\s*" + op_desc_pairs[found_class.group(1)][j_ln][0] + "\s*\(\s*name\s*=\s*\"" +op_desc_pairs[found_class.group(1)][j_ln][1]+ "\"\s*,(.*)"
                        
                        print job_regex
                        while(True):
                            
                            if job_ln==len(f_content):
                                print "failed to find attribute , end of file"
                                break
                            job_fails = re.search('^class\s+([^\(]+)' ,f_content[job_ln])
                            if job_fails:
                                print "failed to find attribute , end of class"
                                break
                            find_op = re.search(job_regex,f_content[job_ln])
                       
                            if find_op:
                                print "FOUND at", job_ln, " trail: ", find_op.group(1)
                                
                                if find_op.group(1).strip()== '':
                                    
                                    print " is multiline "

                                    job_multi_ln= job_ln + 1      
                                    while(True):
                                        if job_multi_ln==len(f_content):
                                            print "failed to find description , end of file"
                                            break
                                        find_op_desc = re.search('^\s+description\s*=\s*"', f_content[job_multi_ln])
                                        fail_op_desc = re.search('\)$', f_content[job_multi_ln].strip() )
                                        if fail_op_desc:
                                            print " there is no description for this op"
                                            f_content.insert(job_ln, re.search('^(\s*)\w',f_content[job_multi_ln +1]  ).group(1) + "description = \"" + op_desc_pairs[found_class.group(1)][j_ln][2] +  "\", \n")
                                            
                                            break
                                        if find_op_desc:
                                            print f_content[job_multi_ln]
                                            new_comment= re.search('^(\s*)\w',f_content[job_multi_ln]).group(1) + "description = \"" + op_desc_pairs[found_class.group(1)][j_ln][2] +  "\", \n"
                                            print new_comment
                                            f_content[job_multi_ln]= new_comment
                                            break
                                        job_multi_ln +=1
                                else :
                                    print "is single line"
                                    
                                    if not re.search('(description\s*=\s*".*)',f_content[job_ln]):
                                        print "no single line description found"
                                        print f_content[job_ln]
                                        new_comment= re.sub('(name\s*=\s*".*"\s*,\s*)', '\\1 description= "' +op_desc_pairs[found_class.group(1)][j_ln][2] + '", ' , f_content[job_ln] )
                                    else:
                                        print "single line has description"
                                        print f_content[job_ln]
                                        new_comment= re.sub('description\s*=\s*".*"\s*,\s*', ' description= "' +op_desc_pairs[found_class.group(1)][j_ln][2] + '", ' , f_content[job_ln] )
                                    f_content[job_ln]= new_comment
                                    print new_comment
                                break
                            job_ln += 1
                            
            outf = open(i, 'w')
            for outl in f_content:
                outf.write(outl)
            outf.close()
        
    else:
        print "didint find any files to look at"                                


