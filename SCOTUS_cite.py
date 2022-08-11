#for case_name in case_name_list:
	#get case info and citation
	#parse citation for relevant info
case_info = dict.fromkeys(['case'])
citation = {
		"volume": None,
		"reporter name": None,
		"first page": None,
		"exact page": None,
		"court name": None,
		"Year": None
		}
		
description = {
			"defendent": None,
			"plantiff": None,
			"summary": None,
			"outcome": None
		}
		
		#example
		
cite_string = "Texas v. Johnson, 491 U.S. 397 (1989)"
	
	# of form Plantiff v. Defendent, Vol. reporter name first page (Year)
dsc_form_list = ["plantiff","defendent"]
cite_form_list = [
	"volume","reporter name", "first page","year"]
dsc, cite= cite_string.split(", ")

dsc_split = dsc.split("v.")
cite = cite.split(" ")

for who, what in zip(dsc_form_list,dsc_split):
	description[who] = what
	
for where, when in zip(cite_form_list,cite):
	citation[where] = when
	
case_info["case"] = {
	dsc:{
		"description":description,
		"citation":citation
		}
	}

print(case_info)
