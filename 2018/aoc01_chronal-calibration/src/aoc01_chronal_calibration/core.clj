(ns aoc01-chronal-calibration.core
  (:use [clojure.string :only (split-lines)]))

(def input (map read-string (split-lines (slurp "01input.txt"))))

; Part 1
(reduce + input)

; Part 2
(defn rotate [seq] (conj (vec (drop 1 seq)) (first seq)))

(defn find-double [input]
  (loop [i 0
         coll (cons (+ (first input) (second input)) '())
         seq (rotate (rotate input))]
    ; check for doubles every 10000 times - because performance
    (if (and (mod i 10000) (empty? (filter #(#{2} (second %)) (frequencies coll))))
      (recur (+ i 1) (conj coll (+ (first coll) (first seq))) (rotate seq))
      (print (filter #(#{2} (second %)) (frequencies coll))))))

(find-double input)
