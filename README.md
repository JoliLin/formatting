formatting
----
+Convert a triple format file into the format of libFM or adjancency list

Example
----
+Input File 
  -- user1,item1,score1
     user2,item2,score3

+Command
  -- python formatting --input <filename> --token , --format FM 
  
Requirements
----
numpy
