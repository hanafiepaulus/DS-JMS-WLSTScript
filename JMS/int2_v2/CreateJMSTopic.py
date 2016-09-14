connect("weblogic", "welcome1", "t3://10.87.225.161:10201")
edit()
startEdit()

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules')
cmo=create('UpdRateTopic','UniformDistributedTopic')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/UniformDistributedTopics/UpdRateTopic')
cmo.setJNDIName('jms.topic.wna.UpdateRate')
cmo.setSubDeploymentName('WNADeployment')

save()
activate()