import os
import os.path
PATH='./labelled_images'
def classification(list_dir): 
  count_undecided=0
  counts={}
  for image in list_dir: 
    try: 
      components=image.split('_')
      if len(components)==1: 
          count_undecided+=1
      else: 
        for component in components[:-1]: 
          counts[component]=counts.get(component, 1)+1
    except: 
      print(f'Something wrong with {image}')
      continue
  counts['undecided']=count_undecided
  return counts

undecided=classification(os.listdir(PATH))
print(undecided)
