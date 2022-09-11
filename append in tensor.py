inps = torch.randn([4,5])
d = torch.randn([1,5])

res = torch.cat([ inps, torch.tensor(d)], dim=0)
#output shape: 5,5

#######################################
##########OOOOOO########OOOOOOO########
#######################################

inps = torch.randn([5,4])
d = torch.randn([5,1])

res = torch.cat([ inps, torch.tensor(d)], dim=-1)
#output shape: 5,5
