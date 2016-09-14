connect("weblogic", "welcome1", "t3://10.87.225.160:10101")
edit()
startEdit()

cd('/SystemResources/BPMModule')
cmo.createSubDeployment('BPMDeployment')

cd('/SystemResources/BPMModule/SubDeployments/BPMDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/CBTResources')
cmo.createSubDeployment('CBTDeployment')

cd('/SystemResources/CBTResources/SubDeployments/CBTDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/CBTSKLRelease')
cmo.createSubDeployment('CBTSKLReleaseSubDeployment')

cd('/SystemResources/CBTSKLRelease/SubDeployments/CBTSKLReleaseSubDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/SAFResources')
cmo.createSubDeployment('SAFDeployment')

cd('/SystemResources/SAFResources/SubDeployments/SAFDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/SiskohatModule')
cmo.createSubDeployment('Siskohat')

cd('/SystemResources/SiskohatModule/SubDeployments/Siskohat')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/TokenJmsModule')
cmo.createSubDeployment('TokenJmsSubDeployment')

cd('/SystemResources/TokenJmsModule/SubDeployments/TokenJmsSubDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))

cd('/SystemResources/WNAModules')
cmo.createSubDeployment('WNADeployment')

cd('/SystemResources/WNAModules/SubDeployments/WNADeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_jms1,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms2,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms3,Type=JMSServer'),ObjectName('com.bea:Name=int_esb1_v2_jms4,Type=JMSServer')], ObjectName))



save()
activate()
