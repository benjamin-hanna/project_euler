#lang racket
(import "imports.scm")

;; Multiples of 3 and 5
;; Problem 1
;; If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
;; Find the sum of all the multiples of 3 or 5 below 1000.

(define (multiples-3-and-5)
    (define (multiples-3-and-5-helper sum count)
        (if (= count 1000)
            sum
            (multiples-3-and-5-helper  
                (cond 
                    ((= (modulo count 3) 0)(+ sum count))
                    ((= (modulo count 5) 0)(+ sum count))
                    (else (+ sum 0)))        
            (+ 1 count))))
(multiples-3-and-5-helper 0 0))
