connect("weblogic", "welcome1", "t3://10.87.225.160:10501")
edit()
startEdit()

cd('/SystemResources/batchResources')
cmo.createSubDeployment('batchSubdeployment')

cd('/SystemResources/batchResources/SubDeployments/batchSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=BatchJMSServer,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer2,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer3,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer4,Type=JMSServer')], ObjectName))

cd('/SystemResources/SAFResources')
cmo.createSubDeployment('SAFDeployment')

cd('/SystemResources/SAFResources/SubDeployments/SAFDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb3_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb3_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb3_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb3_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/WNAModules')
cmo.createSubDeployment('WNADeployment')

cd('/SystemResources/WNAModules/SubDeployments/WNADeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=BatchJMSServer,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer2,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer3,Type=JMSServer'),ObjectName('com.bea:Name=BatchJMSServer4,Type=JMSServer')], ObjectName))



save()
activate()
