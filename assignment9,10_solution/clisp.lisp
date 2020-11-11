(defun nth2 (n lst)
  (if (zerop n)
    (car lst)
    (nth2 (1- n) (cdr lst))))

(write(nth2 6 `(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15)))