(ns aoc02-inventory-management-system.core
  (:use [clojure.string :as str]))

(def input (map read-string (split-lines (slurp "02input.txt"))))

; Part 1
(defn checksum [input]
  (loop [twoletters 0
         threeletters 0
         remaining-ids input]
    (if (not (empty? remaining-ids))
      (let [freqs (frequencies (char-array (str (first remaining-ids))))
            two (if (not (empty? (filter #(#{2} (second %)) freqs))) 1 0)
            three (if (not (empty? (filter #(#{3} (second %)) freqs))) 1 0)]
        (recur (+ twoletters two) (+ threeletters three) (drop 1 remaining-ids)))
      (print (* twoletters threeletters)))))

; Part 2
(defn find-box [input]
  (loop [box-ids input]
    (loop [to-check (first box-ids)
           remaining-ids box-ids]
      (if (not (empty? remaining-ids))
        
        (recur (drop 1 remaining-ids))))

    (recur (drop 1 box-ids))))
