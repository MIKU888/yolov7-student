
import torch
def getMask(x,maskRatio):
    tempx = torch.torch.flatten(x,start_dim=1,end_dim=-1)     #变成[batch,640*640*3]
    print(tempx.shape)
    b,l = tempx.shape
    noise = torch.randn(b,l,device=x.device)
    ids_sort = torch.argsort(noise,dim=1)
    ids_restore = torch.argsort(ids_sort,dim=1)
    mask = torch.zeros(b,l).to(x.device)
    len_keep = l -int(l*maskRatio)
    mask[:,:len_keep]=1
    mask = torch.gather(mask,dim=1,index=ids_restore)
    # maskedX = torch.mul(tempx,mask).unsqueeze(dim=1)
    return mask
x = torch.randn(3,640,640,3)
mask = getMask(x,0.3)
print(x.shape)
print(mask.shape)    #[batch,640*640*3]