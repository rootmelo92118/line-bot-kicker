from linepy import *


client = LINE()
client.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
JoinedGroups = client.getGroupIdsJoined()
print("My MID : " + MySelf.mid)

targets = []


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if op.param1 not in JoinedGroups:
                client.acceptGroupInvitation(op.param1)
                JoinedGroups.append(op.param1)
                client.sendMessage(op.param1, "血盟に荣光あれ☆彡")
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "血盟に荣光あれ☆彡":
                    print "start destroying"
                    _name = msg.text.replace("血盟に荣光あれ☆彡","")
                    group = client.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        client.leaveGroup(msg.to)
                        JoinedGroups.remove(msg.to)
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                               group.name = "血盟に荣光あれ☆彡"
                               client.updateGroup(group)
                               client.leaveGroup(op.param1)
                               JoinedGroups.remove(op.param1)
        else:
            pass
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.SEND_MESSAGE: SEND_MESSAGE
})


while True:
    oepoll.trace()
