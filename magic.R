# Magic Square

magic_4M <- function(n, echo=TRUE){
  # n must be the integer divisible by 4
  if (n %% 4 != 0) warning("To use this method, n must be the integer divisible by 4") 
  else {temp0 <- diag(nrow = 4, ncol = 4) + diag(nrow = 4, ncol = 4)[, 4:1]
        temp1 <- temp0
        p <- n/4
        if (p > 1){
          for (i in 2:p){temp1 <- cbind(temp1, temp0)}
          temp0 <- temp1
          for (i in 2:p){temp1 <- rbind(temp1, temp0)}
        }
        temp2 <- matrix(rep(1, n^2), nrow = n, ncol = n) - temp1 
        result <- matrix(1:n^2, nrow = n, ncol = n, byrow = T) * temp1 + 
                  matrix(n^2:1, nrow = n, ncol = n, byrow = T) * temp2
        Sum <- (n^2 + 1) / 2 * n
        # check the row sum and column sum
        if(all(colSums(result) == Sum) & all(rowSums(result) == Sum)) {
          if(echo){
            cat("Magic square found at the order of", n, "\n")
            print(result)
            cat("Row sum and column sum are both", Sum)
          }
          return(result)
        }        
  }
}

magic_4M
