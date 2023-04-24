from enum import Enum
from collections import namedtuple


Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent type, containing a 'name' field and a 'category' field, with 'category' being of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result of the meeting.
    """
    list_of_active_agents=[]
    out=[]

    for Agent in agent_listing:
        if (Agent[1]==Condition.HEALTHY or Agent[1]==Condition.DEAD):
            out+=[Agent]
        else:
            list_of_active_agents+=[Agent]




    num_of_agent=len(list_of_active_agents)
    #make num of angent even
    if(num_of_agent%2==1):
        num_of_agent-=1
        out+=[list_of_active_agents[-1]]


    for i in range(0,num_of_agent,2):
        A1=list_of_active_agents[i]
        A2=list_of_active_agents[i+1]

        #agent 1 makes 2 feel beter
        if(A1[1]==Condition.CURE):
            if(A2[1]!=Condition.CURE):
                A2=(A2[0],Condition(A2[1].value -1))
        # agent 2 makes 1 feel beter
        elif (A2[1] == Condition.CURE):
            if (A1[1] != Condition.CURE):
                A1 =(A1[0], Condition(A1[1].value - 1))

        # 2 agents are sick
        elif((A1[1] != Condition.CURE) and  (A2[1] != Condition.CURE)):
            A1 = (A1[0], Condition(A1[1].value + 1))
            A2 = (A2[0],Condition(A2[1].value +1))

        out+=[A1]
        out += [A2]
        
    return out
