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
                group = client.getGroup(op.param1)
                for contact in group.members:
                    targets.append(contact.mid)
                if targets == []:
                    client.leaveGroup(op.param1)
                    JoinedGroups.remove(op.param1)
                else:
                        try:
                            kick = [targets]
                            klist = random.choice(kick)
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            client.kickoutFromGroup(op.param1, [klist])
                            print(op.param1, [contact.mid])
                        except:
                            group.name = "血盟に荣光あれ☆彡"
                            client.updateGroup(group)
                            client.leaveGroup(op.param1)
                            JoinedGroups.remove(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def KICKOUT_FROM_GROUP(op):
    try:
        targets.remove(op.param3)
    except Exception as e:
        print(e)
        print("\n\nKICKOUT_FROM_GROUP\n\n")
        return
    
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.KICKOUT_FROM_GROUP: KICKOUT_FROM_GROUP
})


while True:
    oepoll.trace()
