connect("weblogic", "welcome1", "t3://10.87.225.162:10301")
edit()
startEdit()

cd('/')
cmo.createJMSSystemResource('SAFResources')

cd('/SystemResources/SAFResources')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('SMSResources')

cd('/SystemResources/SMSResources')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('WNAModules')

cd('/SystemResources/WNAModules')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

save()
activate()

