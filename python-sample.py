
def wombat(state, time_left):
    # Note that the function name MUST be wombat
    import random
    theAction = ""
    availableActions = ["turn", "shoot", "move"]
    availableMetadata = {"turn": {"direction" : 'right'}, "shoot": {}, "move": {}}
    
    index = random.randint(1,2)
    
    action = availableActions[index]
    metadata = availableMetadata[action]
    
    if state['global-coords'][1] == state['global-dimensions'][1]:
        action = availableActions[0]
        metadata = availableMetadata[action]
    return {
        'command': {
            'action': action,
            'metadata': metadata
        },
        'state': state
    }
