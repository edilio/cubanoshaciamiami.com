def AddNewWebSite(ip, websitename):
    f = open("c:/windows/system32/drivers/etc/Hosts","a")
    f.write("\n%s  %s" %(ip,websitename))
    f.close()

AddNewWebSite("127.0.0.1","www.elmio.com")
AddNewWebSite("87.216.50.179","www.cubanoshaciamiami.com")
#AddNewWebSite("87.216.50.179","www.clasicuba.com")