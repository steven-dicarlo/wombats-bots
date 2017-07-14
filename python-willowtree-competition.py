

def wombat(state, time_left):
    # Note that the function name MUST be wombat
    turnRightAction = {'action': 'turn', 'metadata' : {'direction': 'right'}}
    turnLeftAction = {'action': 'turn', 'metadata' : {'direction': 'left'}}
    moveAction = {'action': 'move', 'metadata': {}}
    shootAction = {'action': 'shoot', 'metadata': {}}


    def updateFacingDirection (currentDirection, action):
    	if action['action'] == 'turn':
    		if action['metadata']['direction'] == 'left':
    			if currentDirection == 'up':
    				return 'left'
    			if currentDirection == 'left':
    				return 'down'
    			if currentDirection == 'down':
    				return 'right'
    			if currentDirection == 'right':
    				return 'up'
    		if action['metadata']['direction'] == 'right':
    			if currentDirection == 'up':
    				return 'right'
    			if currentDirection == 'left':
    				return 'up'
    			if currentDirection == 'down':
    				return 'left'
    			if currentDirection == 'right':
    				return 'down'
		else: 
			return currentDirection
    def blockType(x, y):
		return state['arena'][x][y]['contents']['type']
	
    def blockTypeInFront (currentDirection):
		if currentDirection == 'up':
			return blockType(3,2)
		if currentDirection == 'left':
			return blockType(2,3)
		if currentDirection == 'down':
			return blockType(3,4)
		if currentDirection == 'right':
			return blockType(4,3)
	
    def facingEdge(currentDirection):
		if currentDirection == 'up':
			state['global-coords'][1] == 0
		if currentDirection == 'left':
			state['global-coords'][0] == 0
		if currentDirection == 'down':
			state['global-coords'][1] == (state['global-dimensions'][1] - 1)
		if currentDirection == 'right':
			state['global-coords'][0] == (state['global-dimensions'][0] - 1)
	
    import random
    theAction = ""
    availableActions = [turnRightAction, turnLeftAction, moveAction, shootAction]
    
    if 'saved-state' not in state:
	currentDirection = 'right'
    else:
	currentDirection = state['saved-state']['direction']
    
    # index = random.randint(0,3)
    # action = availableActions[index]
    
   # if state['global-coords'][0] == (state['global-dimensions'][0] - 1) and state['direction'] == "right":
     #   action = availableActions[3]
	
	if facingEdge(currentDirection):
		action = turnRightAction
	else if blockTypeInFront(currentDirection) in ['steel-barrier', 'poison']:
		action = turnRightAction
	else if blockTypeInFront(currentDirection) in ['wood-barrier', 'zakano', 'wombat', 'fog']:
		action = shootAction
	else:
		action = moveAction
		
        
    state['direction'] = updateFacingDirection(currentDirection, action)
    return {
        'command': action,
        'state': state
    }

