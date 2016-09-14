connect("weblogic", "welcome1", "t3://10.87.225.162:10301")
edit()
startEdit()

cd('/SystemResources/SAFResources')
cmo.createSubDeployment('SAFDeployment')

cd('/SystemResources/SAFResources/SubDeployments/SAFDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/SMSResources')
cmo.createSubDeployment('SMSDeployment')

cd('/SystemResources/SMSResources/SubDeployments/SMSDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/WNAModules')
cmo.createSubDeployment('WNADeployment')

cd('/SystemResources/WNAModules/SubDeployments/WNADeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=ext_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=ext_esb1_v2_jms4,Type=JMSServer')], ObjectName))



save()
activate()
