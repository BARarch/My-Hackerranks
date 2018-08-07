(defun fn (n)
    (if (> n 0)
        (progn  (write-line "Hello World")
                (fn (- n 1)))
        ()))

(fn (read))
