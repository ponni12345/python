graph={}
print("\n graph operation:")
graph['A']=['B','C']
graph['B']=['A','D']
graph['C']=['A','D']
graph['D']=['B','C']
print("graph adjancency list:")
for node,neighbores in graph.items():
   print(f"{node}:{neighbores}")    
      
