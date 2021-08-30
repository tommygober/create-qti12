import re, glob, os
from zipfile import ZipFile

counter = 1

target = "*.txt"

def header(testname):
    global counter
    output = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n"
    output += "<questestinterop>\n"
    output += "<assessment title=\""+testname+"\" ident=\"A"+str(counter)+"\">\n"
    counter+=1
    output += "<section title=\"Main\" ident=\"S"+str(counter)+"\">\n"
    counter+=1
    return output

#---------------------------- QUESTION -------------------------------------
def question(name, number, ques_text, choices, correct_choice):
    global counter
    for x in range(0, len(correct_choice)):
        correct_choice[x] = ord(correct_choice[x])-65
    output = ""
    item_names = []
    output += "<item title=\""+name+"-"+number+"\" ident=\"QUE_"+ str(counter) +"\">\n"
    
    counter+=1
    output += "<presentation>\n"
    output += "\t<material>\n"
    output += "\t\t<mattext texttype=\"text/html\"><![CDATA["+ques_text+"]]></mattext>\n"
    output += "\t</material>\n"
    question_name = "QUE_"+str(counter)+"_RL"
    counter+=1
    output += "\t<response_lid ident=\""+question_name+"\" rcardinality=\"Single\" rtiming=\"No\">\n"
    output += "\t<render_choice>\n"
    
    #---------------------------- RESPONSES ------------------------------------------
    opt_num = 1
    for choice in choices:
        item_name = "QUE_"+str(counter)+"_A"+str(opt_num)
        counter+=1
        opt_num+=1
        item_names.append(item_name)
        output += "\t<response_label ident=\""+item_name+"\">\n"
        output += "\t\t<material>\n"
        output += "\t\t\t<mattext texttype=\"text/html\"><![CDATA["+choice+"]]></mattext>\n"
        output += "\t\t</material>\n"
        output += "\t</response_label>\n"
        
    output += "\t</render_choice>\n"
    
    output += "</response_lid>\n"
    output += "</presentation>\n"
    
    output += "<resprocessing>\n"
    output += "\t<outcomes>\n"
    output += "\t\t<decvar vartype=\"Integer\" defaultval=\"0\" varname=\"que_score\"/>\n"
    output += "\t</outcomes>\n"
    answer_counter = 0
    opt_num = 0
    for choice in choices:
        output += "\t<respcondition>\n"
        output += "\t\t<conditionvar>\n"
        output += "\t\t\t<varequal respident=\""+question_name+"\">"+item_names[opt_num]+"</varequal>\n"
        opt_num+=1
        output += "\t\t</conditionvar>\n"
        if(answer_counter in correct_choice):
            output += "\t\t<setvar varname=\"que_score\" action=\"Set\">1</setvar>\n"
        else:
            output += "\t\t<setvar varname=\"que_score\" action=\"Add\">0</setvar>\n"
        output += "\t</respcondition>\n"
        answer_counter+=1
    output += "</resprocessing>\n"
    output += "</item>\n"
    return output

#-------------------------------------------------------------------------------
def footer():
    output = "</section>\n"
    output += "</assessment>\n"
    output += "</questestinterop>\n"
    return output
#-------------------------------------------------------------------------------
def create_manifest(qti_filename, testname):    
    output = "<?xml version=\"1.0\"?>\n"
    output += "<manifest identifier=\"MANIFEST1\" xmlns=\"http://www.imsglobal.org/xsd/imscp_v1p1\" xmlns:imsmd=\"http://www.imsglobal.org/xsd/imsmd_v1p2\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 imsmd_v1p2p2.xsd\">\n"
    output +="<metadata>\n"
    output +="\t\t<schema>IMS Content</schema>\n"
    output +="\t\t<schemaversion>1.1.3</schemaversion>\n"
    output +="\t\t<imsmd:lom>\n"
    output += "\t\t\t<imsmd:general>\n"
    output +="\t\t\t\t<imsmd:identifier>\n"
    output +="\t\t\t\t\t<imsmd:langstring xml:lang=\"en-US\">A6CD294E41BC4C94AE53FE83027BCCF3</imsmd:langstring>\n"
    output +="\t\t\t\t</imsmd:identifier>\n"
    output +="\t\t\t\t<imsmd:title>\n"
    output +="\t\t\t\t\t<imsmd:langstring xml:lang=\"en-US\">"+testname+"</imsmd:langstring>\n"
    output +="\t\t\t\t</imsmd:title>\n"
    output +="\t\t\t</imsmd:general>\n"
    output +="\t\t</imsmd:lom>\n"
    output +="\t</metadata>\n"
    output +="\t<organizations default=\"EXAM1\">\n"
    output +="\t\t<organization identifier=\"EXAM1\" structure=\"hierarchical\">\n"
    output +="\t\t\t<title>default</title>\n"
    output +="\t\t\t<item identifier=\"ITEM1\" identifierref=\"RESOURCE1\">\n"
    output +="\t\t\t\t<title>Exam 1</title>\n"
    output +="\t\t\t</item>\n"
    output +="\t\t</organization>\n"
    output +="\t</organizations>\n"
    output +="\t<resources>\n"
    output +="\t\t<resource identifier=\"RESOURCE1\" type=\"imsqti_xmlv1p1\" href=\""+qti_filename+"\">\n"
    output +="\t\t\t<file href=\""+qti_filename+"\" />\n"
    output +="\t\t</resource>\n"
    output +="\t</resources>\n"
    output +="</manifest>"
    file = open("imsmanifest.xml", "w")
    file.write(output)
    file.close()

    return output

#-------------------------------------------------------------------------------

def getTestName(file):
    testname = file.split("- qti -")
    try:
        testname = testname[1].strip()
    except:
        print("WARNING: No QTI found in filename ", file)
    testname = re.sub(".xml", "", testname)
    testname = re.sub(" qti - ", "", testname)
    testname = re.sub(" ", "_", testname)
    testname = testname.lower()
    #limit length of name to XX characters (unsure of max limit)
    if (len(testname)>20):
        testname = (testname[:20]) if len(testname) > 20 else testname
    return testname

#-------------------------------------------------------------------------------

def create_zip(filename, manifest):
    filename_new = re.sub(".xml", ".zip", filename)
    zipFile = ZipFile(filename_new, "w")
    zipFile.write(filename)
    zipFile.write('imsmanifest.xml')
    zipFile.close()
    print(filename_new + " zipped.")

#-------------------------------------------------------------------------------

for filename_orig in glob.glob(target):
    file_orig = open(filename_orig, "r+", encoding="utf8", errors="ignore")
    filename_new = re.sub(r"(\d+\.\d+\.\d+|Appendix [A-Z])",r"\1 - qti", filename_orig)
    filename_new = re.sub(".txt", ".xml", filename_new)
    testname = getTestName(filename_new)
    
    question_text = ""
    question_number = 1
    answers = []
    correct = []
    line_num = 0
    file = open(filename_new, "w")
    file_out = header(testname)
    for line in file_orig:
        #line_num+=1
        line = line.strip()
        try:
            line = line.encode('ascii','ignore').decode()
        except:
            pass
        #print(line_num, line)
        if re.match("^True", line):
            answers.append("True")
            continue
        if re.match("^False", line):
            answers.append("False")
            continue
        if re.match("^\*True", line):
            answers.append("True")
            correct.append("A")
            continue
        if re.match("^\*False", line):
            answers.append("False")
            correct.append("B")
            continue
        if re.match("^\*[A-Za-z]{1}", line):
            option = re.split("\)|\.|\ ", line, 1)
            #print(option)
            answers.append(option[1].strip())
            correct.append( re.sub("\*","", str(option[0]).upper() ) )
            continue
        if re.match("^[A-Za-z]{1}", line):
            option = re.split("\)|\.|\ ", line, 1)
            #print(option)
            answers.append(option[1].strip())
            continue
        #QUESTION TEXT
        if re.match("^[0-9]", line):
            text = line.split(". ", 1)
            question_text = str(text[1])
            #print(text[1])
            continue
        if re.match(r"^$", line):
            #print("#"+ str(question_number) +": ", question_text,"\n", answers,"\n", correct)
            #XML output
            if (len(question_text)>0) and (len(answers)>0) and (len(correct)>0):
                file_out += question(testname, str(question_number), question_text, answers, correct)
                question_number += 1
            question_text = ""
            answers = []
            correct = []
            #print("---")
            
    file_out += footer()
    file.write(file_out)
    file.close()
    print(filename_new + " created.")
    create_manifest(filename_new, testname)
    print("manifest created.")
    create_zip(filename_new, "imsmanifest.xml")
    os.remove(filename_new)
    os.remove("imsmanifest.xml")
    counter = 1
    file_orig.close()
    print("\n")
#-----------------------------------------------------------------------
#print(filename_new)
#print(file_out)