connect("weblogic", "welcome1", "t3://10.87.225.160:10101")
edit()
startEdit()

cd('/')
cmo.createJMSSystemResource('BPMModule')

cd('/SystemResources/BPMModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('CBTResources')

cd('/SystemResources/CBTResources')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('CBTSKLRelease')

cd('/SystemResources/CBTSKLRelease')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('SAFResources')

cd('/SystemResources/SAFResources')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('SiskohatModule')

cd('/SystemResources/SiskohatModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('TokenJmsModule')

cd('/SystemResources/TokenJmsModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

cd('/')
cmo.createJMSSystemResource('WNAModules')

cd('/SystemResources/WNAModules')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb_cluster,Type=Cluster')], ObjectName))

save()
activate()

