import os

# get a list of all available scans
reports = [dI for dI in os.listdir('../scanReports') if os.path.isdir(os.path.join('../scanReports',dI))]

#copying html code of nmap results to the server folder


# prepare html code to list all reports
html_code = ""
for report in reports :
    html_code += '<a href="server/'+report+'">'+report+'</a><br>\n\t    '

# getting the page model, and adding the html_code of the available scans
page = ""
with open("pagemodel.html","r") as model:
    page = model.read().replace("<!--REPLACE ME-->",html_code)

# write results
with open("server/main.html","w") as main:
    main.write(page)

os.system("sudo python3 -m http.server --directory server/ --bind localhost 80")