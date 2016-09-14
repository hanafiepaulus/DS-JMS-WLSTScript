connect("weblogic", "welcome1", "t3://10.87.225.161:10201")
edit()
startEdit()

cd('/')
cmo.createJMSSystemResource('SAFResources')

cd('/SystemResources/SAFResources')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb2_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('WNAModules')

cd('/SystemResources/WNAModules')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb2_v2_osb_cluster,Type=Cluster')], ObjectName))

save()
activate()

