import numpy as np

def calculate(list):  
    if len(list)<9:
        raise ValueError ("List must contain nine numbers.")
    
    else:
        
        list_matrix = np.reshape(list, (3,3))
        
        mean_axis_one = np.mean(list_matrix, axis=0)
        mean_axis_two = np.mean(list_matrix, axis=1)
        mean_flattened = np.mean(list_matrix)
        mean_values = np.array([mean_axis_one.tolist(), mean_axis_two.tolist(), mean_flattened.tolist()])



        variance_axis_one = np.var(list_matrix, axis=0)
        variance_axis_two = np.var(list_matrix, axis=1)
        variance_axis_flattened = np.var(list_matrix)
        variance_values = np.array([variance_axis_one.tolist(), variance_axis_two.tolist(), variance_axis_flattened.tolist()])

        
        standdev_axis_one = np.std(list_matrix, axis=0)
        standdev_axis_two = np.std(list_matrix, axis=1)
        standdev_axis_flattened = np.std(list_matrix)
        standdev_values = np.array([standdev_axis_one.tolist(), standdev_axis_two.tolist(), standdev_axis_flattened.tolist()])

        
        max_axis_one = np.max(list_matrix, axis=0)
        max_axis_two = np.max(list_matrix, axis=1)
        max_axis_flattened = np.max(list_matrix)
        max_values = np.array([max_axis_one.tolist(), max_axis_two.tolist(), max_axis_flattened.tolist()])

        
        min_axis_one = np.min(list_matrix, axis = 0)
        min_axis_two = np.min(list_matrix, axis = 1)
        min_axis_flattened = np.min(list_matrix)
        min_values= np.array([min_axis_one.tolist(), min_axis_two.tolist(), min_axis_flattened.tolist()])
        


        sum_axis_one = np.sum(list_matrix, axis = 0)
        sum_axis_two = np.sum(list_matrix, axis = 1)
        sum_axis_oflattened = np.sum(list_matrix)
        sums_values = np.array([sum_axis_one.tolist(), sum_axis_two.tolist(), sum_axis_oflattened.tolist()])
        
        
        mean1 = mean_values.tolist()
        mean = f"mean: {mean1}"
        
        variance1 = variance_values.tolist()
        variance = f"variance: {variance1}"
        
        standard_deviation1 = standdev_values.tolist()
        standard_deviation = f"standard deviation: {standard_deviation1}"
        
        maxi1 = max_values.tolist()
        maxi = f"max: {maxi1}"
        
        mini1 = min_values.tolist()
        mini = f"min: {mini1}"
        
        sumi1 = sums_values.tolist()
        sumi = f"sum: {sumi1}"
        
        
        calculations = mean + "\n" + variance + "\n" + standard_deviation + "\n" + maxi +"\n" + mini +"\n" +sumi
        
        calculation = dict({"mean":  mean_values.tolist(),
                       "variance": variance_values.tolist(),
                       "standard deviation": standdev_values.tolist(),
                       "max": max_values.tolist(),
                       "min" : min_values.tolist(),
                       "sum" : sums_values.tolist()
                                                   
                      })
     
        return calculation


    