from html.parser import HTMLParser 

def txtparser(file_name):
    with open(file_name,"r") as reader:
        textinfile = reader.read()
        print("\n Parsing info: ", file_name,"\n")
        twords = textinfile.split()
        print("total words = ",len(twords))
        tlines = textinfile.count("\n")
        print ("total line = ",tlines+1)
        tspaces = textinfile.count(" ")
        print("total spaces = ",tspaces )
        ttabs = textinfile.count("\t")
        print("total tabs = ", ttabs)
        tparas = textinfile.count("\n\n") + 1 
        print("total paragrapghs = ", tparas)



def HTML_parser(file_name):
    with open(file_name,"r") as hf_r:
            text_in_file = hf_r.read()
            tags_encountered = []
            class Parser(HTMLParser):
                def handle_starttag(self,tag,attrs):
                    tags_encountered.append(tag)
                def handle_endtag(self,tag):
                    tags_encountered.append(tag)
            ParserInit = Parser()
            ParserInit.feed(text_in_file)
            tags_with_occurance = {}
            for i in range(len(tags_encountered)):
                under_observation = tags_encountered[i]
                total_occurance = 0
                for j in range(len(tags_encountered)):
                    if tags_encountered[j] == under_observation:
                        total_occurance = total_occurance + 1
                    tags_with_occurance [under_observation] = [total_occurance]
            print("Parsing HTML file: ",file_name,"\n")
            for each_key,each_value in tags_with_occurance.items():
                print("\nTag \"",each_key,"\" occurs ",each_value," times.")

print ("\nWhat do you want to Parse? (Select an option)\n\n\t(1) Text file (2) HTML file")
usr_input = int(input("\nOption number --> "))

if usr_input == 1:
    file_path = input ("\nEnter the path of the file: ")
    txtparser(file_path)
elif usr_input == 2:
    file_path = input("\nEnter the path of the file: ")
    HTML_parser(file_path)
