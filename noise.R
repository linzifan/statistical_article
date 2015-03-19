library(jpeg)
pic <- readJPEG("cmandenoisy.jpg")
h <- 0.1  #h=0.5, h=1, h=5, h=10
gaukernel.fit <- matrix(0,256,256)
for(j in 1:256){
    for(i in 1:256){
        #for a certain pixel, find a block size 3*3 around it
        nbij<-rbind(c(i,j),expand.grid(max(1,i-1):min(i+1,256),max(1,j-1):min(j+1,256)))
        #for a certain pixel, find a block size 9*9 around it
        #nbij<-rbind(c(i,j),expand.grid(max(1,i-4):min(i+4,256),max(1,j-4):min(j+4,256)))
        #calculate distance between the certain pixel and each points in the block
        distij<-as.matrix(dist(nbij))[-1,1]
        #Gaussian kernel
        Kij<-exp(-distij^2/(2*h^2))
        yij<-pic[max(1,i-4):min(i+4,256),max(1,j-4):min(j+4,256)]
        yij<-as.vector(yij)
        gaukernel.fit[i,j]<-Kij%*%yij/sum(Kij)
    }
}
writeJPEG(gaukernel.fit,"cman9x9h10.jpeg")
