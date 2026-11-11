import jsoninterface as ji

ji.jsoninterface.addcomponnent("data/tempdata.json", "V1.0", "Version")
print (ji.jsoninterface.getfilecomponent("data/echo.json", "desc@flags@H"))