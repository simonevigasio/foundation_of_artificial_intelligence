# Import the CSP (Constraint Satisfaction Problem) class for implementing backtracking algorithms.
from init import CSP

def backtracking(csp: CSP, assignment):
    """Perform a recursive backtracking search to find a solution to the CSP (Constraint Satisfaction Problem)."""

    # Check if the assignment is complete (i.e., all variables are assigned values satisfying the CSP).
    if csp.is_goal(assignment): 
        return assignment
    
    # Select an unassigned variable based on the CSP's variable selection heuristic.
    var = csp.select_unassigned_variable(assignment=assignment)

    # Iterate over each possible value for the selected variable, ordered by the CSP's domain value heuristic.
    for value in csp.order_domain_values(var=var, assignment=assignment):

        # Check if assigning this value to the variable is consistent with the current assignment.
        if csp.is_consistent(var=var, value=value, assignment=assignment):

            # Temporarily add this value to the variable in the assignment.
            csp.add_value(var=var, value=value, assignment=assignment)

            # Recursively attempt to complete the assignment with the updated partial assignment.
            result = backtracking(csp, assignment=assignment)

            # If a complete assignment was found (i.e., result is not failure), return the successful assignment.
            if result != csp.failure:
                return result 
            
            # If no solution was found with this value, remove the variable's value from the assignment (backtrack).
            csp.remove_value(var=var, assignment=assignment)

    # Return failure if no valid assignment can be found for the current variable's domain values.
    return csp.failure 

def backtracking_search(csp: CSP):
    """Initiate a backtracking search for a solution to the CSP."""

    # Start the backtracking search with the initial assignment provided by the CSP instance.
    return backtracking(csp=csp, assignment=csp.initial)