
#Institute -: Logic Mojo
#Dated 18-OCT-2026 (Sunday)
#Instructor -: Mahipal Singh Shekhawat 
#Student -: Nikhil Srivastava



# ============================================================
# PYTHON DATA STRUCTURES PRACTICE QUESTIONS
# Topics: List, Tuple, Set, Dictionary
# Total Questions: 40
# ============================================================


# ============================================================
# SECTION 1: LISTS (Questions 1-10)
# ============================================================

# Q1. Create a list named model_scores containing the accuracy
# scores of three machine learning models: 85, 90, and 88.
# Print the list and its length.

class parentlist:
    def __init__(self):
        self.model_scores = [85, 90, 88]

class childlist(parentlist):
    def show(self):
        length = len(self.model_scores)
        print(f"The length of list model_scores : {length}")

l2 = childlist()
l2.show()
    
# Q2. A dataset contains the following feature names:
# ["age", "salary", "experience", "education"]
# Print the first feature, the last feature, and the total
# number of features.

class features:
    def __init__(self, datasetlist = None):
        self.datasetlist = datasetlist

class printfeatures(features):
    def printfeatures(self):
        if not self.datasetlist:
            print("No features available.")
            return
        print(f"First feature: {self.datasetlist[0]} and last feature: {self.datasetlist[-1]}")
        print(f"Total number of features: {len(self.datasetlist)}")

pftures = printfeatures(["age", "salary", "experience", "education"])
pftures.printfeatures()

# Q3. A machine learning model produces the following predictions:
# [1, 0, 1, 1, 0]
# Add a new prediction, 1, to the list.
# Then remove the first occurrence of 0 and print the list.
class predictions:
    def __init__(self, predictionlist=None):
        self.predictionlist = list(predictionlist) if predictionlist is not None else []

class predictionoperations(predictions):
    def addnew (self,item):
        self.predictionlist.append(item)

    def foccurence (self,fcitem):
        self.predictionlist.remove(fcitem)
               

class predictionsshow(predictionoperations):
    def showpre(self):
        print(f"Items in the list are : {self.predictionlist}")

c3 = predictionsshow([1, 0, 1, 1, 0])
c3.showpre()
c3.addnew(1)
c3.showpre()
c3.foccurence(0)
c3.showpre()


# Q4. A dataset contains missing-value counts for five columns:
# [12, 0, 8, 5, 0]
# Add the missing-value count of 3 for a new column.
# Replace the count at index 0 with 10.
# Remove all columns whose missing-value count is 0.
# Print the final list.

class missingvalue:
    def __init__(self, mvdataset=None):
        self.mvdataset = list(mvdataset) if mvdataset is not None else [] 
class missingvalueopr(missingvalue):
    def addmissingvalue(self, item):
        self.mvdataset.append(item)
    def missingvalerep(self, item):
        self.mvdataset[0]=item
    def missingvalueremove_zeros(self):
         i = 0
         while i in self.mvdataset:
             self.mvdataset.remove(i)
class showlist(missingvalueopr):
    def showl(self):
        print(f"The item in the list mvdataset : {self.mvdataset}")   
class destroyobj(showlist):
    def __delete__(self, instance):
        print(f"{instance} Object Destroyed")                    
    
c3 = showlist([12, 0, 8, 5, 0])
c3.showl()
c3.addmissingvalue(3)
c3.showl()
c3.missingvalerep(10)
c3.showl()
c3.missingvalueremove_zeros()
c3.showl()
c3 = " "
c4 = destroyobj(c3)
c4.__delete__(c3)

# Q5. You have the following model accuracy scores:
# [0.82, 0.91, 0.87, 0.95, 0.89]
# Sort the scores in descending order.
# Print the highest and lowest scores.
# Also print the top three scores.

class accuracyscores:
    def __init__(self, listdataset1=None):
        self.listdataset1 = list(listdataset1) if listdataset1 is not None else []
class accuracyopr(accuracyscores):
    def sort(self):
        return self.listdataset1.sort(reverse="true")
    def highest(self):
        self.hvalue = max(self.listdataset1)
        return self.hvalue     
    def lowest(self):
        self.lvalue = min(self.listdataset1)     
        return self.lvalue
    def top3(self):
        self.top3 = []
        self.listdataset1.sort(reverse="true")
        self.top3=self.listdataset1[:3]
        return self.top3
class showopr(accuracyopr):
    def show(self):
        print(f"{self.listdataset1}")
        print(f"Highest Value : {self.hvalue}")
        print(f"Lowest Value : {self.lvalue}")
        print(f"Top Three : {self.top3}")
c3 = showopr([0.82, 0.91, 0.87, 0.95, 0.89])
c3.sort()
c3.highest()
c3.lowest()
c3.top3()
c3.show()

# Q6. A dataset contains the following customer ages:
# [25, 32, 45, 28, 36, 50, 22, 41]
# Create a new list containing only ages greater than or equal
# to 30 using a loop or list comprehension.
# Print the filtered list.

class custages:
    def __init__(self,cages=None):
        self.cages = list(cages) if cages is not None else []
class cagesopr(custages):
    newlist = []
    def fileteragesgreaterthan30(self):
        i = 0
        for i in self.cages:
            if i>=30:
                self.newlist.append(i)
        return self.newlist
class show(cagesopr):
    def show(self):
        print(f"{self.newlist}")
c3 = show([25, 32, 45, 28, 36, 50, 22, 41])
c3.fileteragesgreaterthan30()
c3.show()

# Q7. A model has produced the following actual and predicted
# labels:
#
# actual_labels = [1, 0, 1, 1, 0, 1]
# predicted_labels = [1, 0, 0, 1, 0, 1]
#
# Create a list containing 1 when the actual and predicted
# labels match and 0 when they do not.
# Print the resulting list.
class acpre:
    def __init__(self,actual,predicted):
        self.actual = list(actual)if actual is not None else []
        self.predicted = list(predicted)if predicted is not None else []
class compareacpre(acpre):
    newlist = []
    i = 0
    def compare(self):
        while self.i<=len(self.actual)-1:
                if self.actual[self.i] == self.predicted[self.i]:
                    self.newlist.append(1)
                else:
                    self.newlist.append(0)
                self.i = self.i + 1    
        return self.newlist
class show(compareacpre):
    def showlist(self):
        print(f"{self.newlist}")                
c3 = show([1, 0, 1, 1, 0, 1],[1, 0, 0, 1, 0, 1])
c3.compare()
c3.showlist()

# Q8. A dataset contains the following feature values:
# [10, 20, 30, 40, 50, 60]
# Split the list into two separate lists:
# - The first list should contain the first three values.
# - The second list should contain the remaining values.
# Print both lists.
class listdataset:
    def __init__(self,list1 = None,list2 = None):
        self.list1 = list(list1) if list1 is not None else []
        self.list2 = list(list2) if list2 is not None else []
class sepratelist(listdataset):
    list3 = []
    list4 = []
    def sep(self):
        self.list3 = self.list1[:3]
        self.list4 = self.list1[3:]
        return self.list3
        return self.list4
class printlist(sepratelist):
    def printlists(self):
        print(f"{self.list3}")    
        print(f"{self.list4}")   

c3 = printlist([10, 20, 30, 40, 50, 60])
c3.sep()
c3.printlists()


# Q9. A data scientist has collected the following model scores:
# [0.75, 0.82, 0.91, 0.68, 0.88, 0.95, 0.79]
#
# Calculate the average score using the list.
# Create another list containing only scores above the average.
# Print the average and the filtered list.
class listdataset:
    def __init__(self, scores = None):
        self.scores = list(scores) if scores is not None else []
class listdatasetopr(listdataset):
    avg = 0.00
    i=0.00
    newlist = []
    def findavg(self):
        self.avg = sum(self.scores)/len(self.scores)
        return self.avg
    def aboveavg(self):
        for i in self.scores:
            if i > self.avg:
                self.newlist.append(i)
        return self.newlist
class printlist(listdatasetopr):
    def show(self):
        print(f"Average = {self.avg}")  
        print(f"New List = {self.newlist}")  

c3 = printlist([0.75, 0.82, 0.91, 0.68, 0.88, 0.95, 0.79])
c3.findavg()
c3.aboveavg()
c3.show()        

# Q10. A dataset contains duplicate customer ages:
# [25, 30, 25, 40, 30, 35, 45, 40]
#
# Create a new list containing only unique ages while
# preserving their original order.
# Then sort the unique ages in ascending order.
# Print both the unique list and the sorted list.
class listdataset:
    def __init__(self, cages = None):
        self.cages = list(cages) if cages is not None else []
class removeduplicate(listdataset):
    newlist = []
    def uniquedataset(self):
        seen = set()
        for i in self.cages:
            if i not in seen:
                self.newlist.append(i)
                seen.add(i)
        return self.newlist
    def sortunique(self):
        return self.newlist.sort()             
class printlist(removeduplicate):
    def printl(self):
        print(f"{self.newlist}") 

c3 = printlist([25, 30, 25, 40, 30, 35, 45, 40])
c3.uniquedataset()
c3.printl()
c3.sortunique()
c3.printl()



# ============================================================
# SECTION 2: TUPLES (Questions 11-20)
# ============================================================

# Q11. Create a tuple named dataset_dimensions containing
# the number of rows and columns in a dataset:
# (1000, 8)
# Print the number of rows and columns separately.

class toupleexample:
    def __init__(self):
        self.dataset_dimensions = (1000, 8)
class printtouple(toupleexample):
    def show(self):
        rows, columns = self.dataset_dimensions
        print(f"Rows: {rows} and Columns: {columns}")

c2 = printtouple()
c2.show()

# Q12. A machine learning model has the following evaluation
# metrics stored in a tuple:
# (0.92, 0.88, 0.90)
#
# The values represent precision, recall, and F1-score.
# Print each metric separately using tuple indexing.

class toupleexample2:
    def __init__(self):
        self.evaluationmetric = (0.92, 0.88, 0.90)
class printtoupleusingidx(toupleexample2):
    def show(self):
        for idx, value in enumerate(self.evaluationmetric):
            if idx == 0:
                print(f"At {idx} index the precision = {value}")
            elif idx == 1:     
                print(f"At {idx} index  the recall = {value}") 
            elif idx == 2:
                print(f"At {idx} index  the F1-score = {value}")          

c2 = printtoupleusingidx()
c2.show()               


# Q13. Create a tuple containing the names of three algorithms:
# ("Linear Regression", "Decision Tree", "Random Forest")
#
# Print the first and last algorithm.
# Also print the length of the tuple.

class algorithmstype:
    def __init__(self):
        self.alogotypes = ("Linear Regression", "Decision Tree", "Random Forest")
class printfunction(algorithmstype):
    def firstlast(self):
        first, middle, last = self.alogotypes
        print(f"First algo = : {first} ")        
        print(f"Last algo = : {last} ")    
    def lengthtouple(self):
        print(f"Length of the touple = : {len(self.alogotypes)}")

c2 = printfunction()
c2.firstlast()
c2.lengthtouple()  

# Q14. The following tuple stores the performance of a model:
# model_metrics = (0.91, 0.87, 0.89, 0.93)
#
# Convert the tuple into a list.
# Replace the second value with 0.90.
# Convert the updated list back into a tuple.
# Print the final tuple.

class modelperformance:
    def __init__(self):
        self.model_metrics = (0.91, 0.87, 0.89, 0.93)
class touipleopr(modelperformance):
    def operationtouple(self):
        mylist = list(self.model_metrics)
        mylist[1] = 0.90
        mytouple = tuple(mylist)
        print(f"Final tuple = : {mytouple}")

c2 = touipleopr()
c2.operationtouple()

# Q15. A dataset has the following feature names:
# ("age", "salary", "experience", "age", "department", "age")
#
# Count how many times "age" appears in the tuple.
# Find the index of its first occurrence.
# Print both results.

class featurenames:
    def __init__(self):
        self.f_names = ("age", "salary", "experience", "age", "department", "age")
class tupleopr(featurenames):
    def countage(self):
        count = 0
        for i in self.f_names:
            if i == "age":
                count = count + 1
        for idx, j in enumerate(self.f_names):
                    if i == "age":
                         break
        print(f"First Occurence of age at index : {idx}")
        print(f"Total Count of Age = : {count}")

c2 = tupleopr()
c2.countage()
       

# Q16. Two machine learning models have the following metrics:
#
# model_a = (0.85, 0.80, 0.82)
# model_b = (0.90, 0.87, 0.88)
#
# Each tuple contains accuracy, precision, and recall.
# Combine the two tuples into a single tuple.
# Print the combined tuple and its length.

class toupleexample3:
    def __init__(self):
        self.model_a = (0.85, 0.80, 0.82)
        self.model_b = (0.90, 0.87, 0.88)
class mergetuples(toupleexample3):
    def mergetuple(self):
        self.newtuple = self.model_a + self.model_b
        return self.newtuple
    def lengthoftuple(self):
        return len(self.newtuple)
class printopr(mergetuples):
    def show(self):
        print(f"Combined Tuple : {self.mergetuple()}")
        print(f"Combined Tuple Length : {self.lengthoftuple()}")  
c3 = printopr()
c3.show()

# Q17. A dataset contains the following feature values:
# feature_values = (10, 20, 30, 40, 50, 60, 70, 80)
#
# Extract the first four values.
# Extract the last three values.
# Extract every second value using slicing.
# Print all three results.

class tupleexample4:
    def __init__(self):
        self.feature_values = (10, 20, 30, 40, 50, 60, 70, 80)
class tupleopr(tupleexample4):
    def first4(self):
        self.f4 = self.feature_values[:4]
        return self.f4
    def last3(self):
        self.l3 = self.feature_values[-3:]
        return self.l3 
    def everySecond(self):
        self.e2 = self.feature_values[::2]
        return self.e2
class printopr(tupleopr):
    def show(self):
        print(f"Fisrt 4 Elements = : {self.first4()}")
        print(f"Last 3 Elements = : {self.last3()}")
        print(f"Every Seconf Element = : {self.everySecond()}") 

c3 = printopr()
c3.show()
    

# Q18. A data scientist stores the following information
# about a trained machine learning model:
#
# model_info = ("Random Forest", 100, 0.94, "Approved")
#
# Unpack the tuple into four variables:
# algorithm, number_of_trees, accuracy, and status.
# Print each variable with a meaningful message.

class toupleexample5:
    def __init__(self):
        self.model_info = ("Random Forest", 100, 0.94, "Approved")        
class fetchvalue(toupleexample5):
    def ftouple(self):
        algorithm, number_of_trees, accuracy, status = self.model_info
        print(f"Algo used for the Model : {algorithm}")
        print(f"Number of Trees in the Algo : {number_of_trees}")
        print(f"Model Accuracy : {accuracy}")
        print(f"Model Status : {status}")
c2 = fetchvalue()
c2.ftouple()           

# Q19. A model evaluation system stores the following results:
#
# evaluation_results = (
#     ("Model A", 0.85),
#     ("Model B", 0.91),
#     ("Model C", 0.88),
#     ("Model D", 0.95)
# )
#
# Each inner tuple contains a model name and its accuracy.
# Print the name and accuracy of every model.
# Then identify and print the name of the model with
# the highest accuracy.

class toupleexample6:
    def __init__(self):
        self.evaluation_results = (
        ("Model A", 0.85),
        ("Model B", 0.91),
        ("Model C", 0.88),
        ("Model D", 0.95)
         )
class printtouple(toupleexample6):
    def printt(self):
        for mname, maccuracy in self.evaluation_results:
            print(f"Model Name : {mname} and Model Accuracy : {maccuracy}")
    def haccuracy(self):
        highestAccuracy = max(self.evaluation_results, key = lambda x: x[1])[0]
        print(f"Model Name with Highest Accuracy : {highestAccuracy}") 

c2 = printtouple()
c2.printt()
c2.haccuracy()

# Q20. A dataset's metadata is stored in the following tuple:
#
# dataset_info = ("Customer Churn", 5000, 12, "Classification")
#
# Create a new tuple that adds the information
# "Version 2.0" at the end.
# Then unpack the new tuple into five variables.
# Print all five values.

class tupleexample7:
    def __init__(self):
        self.dataset_info = ("Customer Churn", 5000, 12, "Classification")
class tupleopr(tupleexample7):
    def topr(self):
        list1 = list(self.dataset_info)
        list1.append("Version 2.0")
        tuple1 = tuple(list1)
        cchurn, val1, val2, classi, version1 = tuple1
        print(f"{cchurn} : {val1} : {val2} : {classi} : {version1}") 
c2 = tupleopr()
c2.topr()

# ============================================================
# SECTION 3: SETS (Questions 21-30)
# ============================================================

# Q21. Create a set containing the following feature names:
# {"age", "salary", "age", "experience", "salary"}
#
# Print the set and observe how duplicate values are handled.

class setexample:
    def __init__(self):
        self.fnames = {"age", "salary", "age", "experience", "salary"}
class printopr(setexample):
    def show(self):
        print(f"Set Elements : {self.fnames}")
c2 = printopr()
c2.show()        

# Q22. A dataset contains the following categories:
# {"Finance", "Healthcare", "Retail"}
#
# Add "Education" to the set.
# Remove "Retail" from the set using discard().
# Print the updated set.

class setsexample2:
    def __init__(self):
        self.datasetcategory = {"Finance", "Healthcare", "Retail"}
class setopr(setsexample2):
    def addelement(self):
        self.datasetcategory.add("Education")
    def removeelement(self):
        self.datasetcategory.discard("Retail")
class printopr(setopr):
    def printset(self):
        print(f"Set Final Elements : {self.datasetcategory}")
    def __del__(self):
        print(f"Object Destrioyed")


c3 = printopr()
c3.printset()
c3.addelement()
c3.printset()
c3.removeelement()
c3.printset() 
del c3

# Q23. Two datasets contain the following feature names:
#
# dataset_a = {"age", "salary", "experience"}
# dataset_b = {"age", "department", "salary"}
#
# Find and print the features common to both datasets.

class setexample4:
    def __init__(self):
          self.dataset_a = {"age", "salary", "experience"}
          self.dataset_b = {"age", "department", "salary"}
class commonsetelements(setexample4):
     def celements(self):
          print(f"Common Elements Are : {self.dataset_a & self.dataset_b}")
     def __del__(self):
          print(f"Object Destroyed")
c2 = commonsetelements()
c2.celements()
del c2          

     
# Q24. Two machine learning projects use the following algorithms:
#
# project_a = {"Linear Regression", "Decision Tree",
#               "Random Forest", "SVM"}
#
# project_b = {"Random Forest", "SVM", "KNN", "Naive Bayes"}
#
# Find and print:
# 1. Algorithms used in both projects.
# 2. Algorithms used only in project_a.
# 3. All unique algorithms used across both projects.

class setaxample5:
    def __init__(self):
        self.project_a = {"Linear Regression", "Decision Tree", "Random Forest", "SVM"}
        self.project_b = {"Random Forest", "SVM", "KNN", "Naive Bayes"}
class setopr(setaxample5):
    def commoninboth(self):
        print(f"Common Algos : {self.project_a & self.project_b}")
        print(f"Difference Algos : {self.project_a - self.project_b}")
        print(f"Unique Elements : {self.project_a | self.project_b}")
    def __del__(self):
        print(f"Object Destroyed ")
c2 = setopr()
c2.commoninboth()
del c2      

# Q25. A data preprocessing pipeline detects missing values
# in the following columns:
#
# missing_dataset_a = {"age", "salary", "experience"}
# missing_dataset_b = {"salary", "department", "experience"}
#
# Find the union and intersection of the two sets.
# Print both results and explain what each represents
# in this missing-data scenario.

class setsexaple6:
    def __init__(self):
        self.missing_dataset_a = {"age", "salary", "experience"}
        self.missing_dataset_b = {"salary", "department", "experience"}
class setopr(setsexaple6):
    def unionelements(self):
        print(f"Unique in both plus duplicates will appear only Once : {self.missing_dataset_a | self.missing_dataset_b}")
    def intersetelements(self):
        print(f"Only common will appear once and completely the duplicates will be Avoided : {self.missing_dataset_a & self.missing_dataset_b}") 
    def __del__(self):
        print(f"Object Destroyed")
c2 = setopr()
c2.unionelements()
c2.intersetelements()
del c2

# Q26. Two teams have selected features for a churn prediction
# model:
#
# selected_features = {"age", "salary", "tenure",
#                      "monthly_charges", "contract"}
#
# removed_features = {"salary", "contract"}
#
# Create a new set containing only selected features that
# are not present in removed_features.
# Print the final feature set.

class setexample7:
    def __init__(self):
        self.selected_features = {"age", "salary", "tenure", "monthly_charges", "contract"}
        self.removed_features = {"salary", "contract"}
class setopr(setexample7):
    def removefeatures(self):
        self.newfeaturelist = set(self.selected_features - self.removed_features)
        #print(f"{type(self.newfeaturelist)}")
        return self.newfeaturelist
class printopr(setopr):
    def show(self):
        print(f"Elements for New Features are : {self.removefeatures()}")
    def __del__(self):
        print(f"Object Deleted")
c3 = printopr()
c3.show()
del c3            
    
        

# Q27. A data scientist has identified the following
# categorical values in two batches of customer data:
#
# batch_1 = {"Gold", "Silver", "Bronze", "Gold"}
# batch_2 = {"Silver", "Platinum", "Bronze"}
#
# Find all unique customer categories across both batches.
# Then find the categories that appear in both batches.
# Print the total number of unique categories.

class setexample8:
    def __init__(self):
         self.batch_1 = {"Gold", "Silver", "Bronze", "Gold"}
         self.batch_2 = {"Silver", "Platinum", "Bronze"}
class setopr(setexample8):
    def uniquecust(self):
        self.uc = set(self.batch_1 | self.batch_2)
        return self.uc
    def commoncust(self):    
        self.cc = set(self.batch_1 & self.batch_2) 
        return self.cc
    def findlen(self):       
        self.lenuc = len(self.commoncust())
        return self.lenuc 
class printopr(setopr):
    def show(self):
        print(f"{self.uniquecust()}")
        print(f"{self.commoncust()}")
        print(f"{self.findlen()}")
    def __del__(self):
        print("Object Deleted")

c3 = printopr()
c3.show()
del c3    

# Q28. A machine learning pipeline supports the following
# preprocessing techniques:
#
# available = {"Scaling", "Encoding", "Imputation",
#              "Feature Selection", "Normalization"}
#
# selected = {"Scaling", "Encoding", "Imputation"}
#
# Check whether selected is a subset of available.
# Check whether available is a superset of selected.
# Also determine which techniques have not been selected.

class setexample9:
    def __init__(self):
        self.selected = {"Scaling", "Encoding", "Imputation"}
        self.available = {"Scaling", "Encoding", "Imputation","Feature Selection", "Normalization"}
class subsetsuperset(setexample9):
    def issubset(self):
        self.subsetexample = self.selected - self.available
        if len(self.subsetexample) == 0 :
            print(f"selected is a subset of available")
    def issuperset(self):
        self.subsetexample = self.selected - self.available
        self.supersetexample = self.available - self.selected
        if len(self.subsetexample) == 0 and len(self.supersetexample)>0:
            print(f"available is a superset of selected")
    def remainingelements(self):
        self.supersetexample = self.available - self.selected
        print(f"Left elements for Selected : {self.supersetexample}")           
    def __del__(self):
        print(f"Object Deleted")
c2 = subsetsuperset()
c2.issubset()
c2.issuperset()
c2.remainingelements()
del c2

# Q29. Two models use the following input features:
#
# model_a_features = {"age", "salary", "tenure",
#                     "credit_score", "balance"}
#
# model_b_features = {"age", "salary", "tenure",
#                     "department", "region"}
#
# Find the common features and the features unique to each
# model.
# Calculate the Jaccard similarity between the feature sets.
#
# Formula:
# Jaccard Similarity = Size of Intersection / Size of Union

class setexample10:
    def __init__(self):
        self.model_a_features = {"age", "salary", "tenure", "credit_score", "balance"}
        self.model_b_features = {"age", "salary", "tenure", "department", "region"}
class setopr(setexample10):
    def unionexample(self):
        self.com_unique = self.model_a_features | self.model_b_features
        print(f"The common features and the features unique to each model : {self.com_unique}")
    def __del__(self):
        print(f"Object Destroyed")
class Jaccard(setexample10):
    def Jaccardsimilarity(self):
        self.js = len(self.model_a_features & self.model_b_features)/len(self.model_a_features | self.model_b_features)         
        print(f"Jaccard Similarity : {self.js}")
    def __del__(self):
            print(f"Object Destroyed")

c2 = setopr()
c2.unionexample()
c3 = Jaccard()
c3.Jaccardsimilarity()
del c2
del c3               

# Q30. A dataset contains the following predicted customer
# segments from two different clustering models:
#
# model_a_segments = {"Low Risk", "Medium Risk", "High Risk"}
# model_b_segments = {"Low Risk", "Medium Risk", "Very High Risk"}
#
# Find:
# 1. Common segments.
# 2. Segments unique to model_a_segments.
# 3. Segments unique to model_b_segments.
# 4. All unique segments across both models.
#
# Finally, add "Critical Risk" to model_b_segments
# and print the updated set.

class setexample11:
    def __init__(self):
        self.model_a_segments = {"Low Risk", "Medium Risk", "High Risk"}
        self.model_b_segments = {"Low Risk", "Medium Risk", "Very High Risk"}
class setoperations(setexample11):
    def segmnts(self):
        print(f"Common Segments : {self.model_a_segments & self.model_b_segments}")
        print(f"Segments unique to model_a_segments : {self.model_a_segments - self.model_b_segments}")
        print(f"Segments unique to model_b_segments : {self.model_b_segments - self.model_a_segments}")
        print(f"All unique segments across both models : {self.model_a_segments ^ self.model_b_segments}")
    def __del__(self):
        print(f"Object Deleted")
class addelement(setexample11):
    def addele(self):
        self.model_b_segments.add("Critical Risk")
        print(f"Final elements for model_b_segments : {self.model_b_segments}")
    def __del__(self):
            print(f"Object Deleted")

c2 = setoperations()
c2.segmnts()
c3 = addelement()
c3.addele()
del c2
del c3      

# ============================================================
# SECTION 4: DICTIONARIES (Questions 31-40)
# ============================================================
from abc import ABC, abstractmethod
class Dictionariesimplementation(ABC):
    @abstractmethod
    def dictionaryinitialization(self):
        pass
    def dictExamples(self):
        pass
    def printresults(self):
        pass

# Q31. Create a dictionary named student_info with the
# following information:
#
# name: "Rahul"
# age: 25
# course: "Data Science"
#
# Print the student's name, age, and course separately.

class student_infoinit(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.student_info = {"name" : "Rahul", "age" : 25, "course" : "Data Science"}
        return self.student_info    
    def printresults(self):
        print(f"Student Name : {self.dictionaryinitialization().get("name")}")
        print(f"Student Age : {self.dictionaryinitialization().get("age")}")
        print(f"Student Course : {self.dictionaryinitialization().get("course")}") 
    def __del__(self):
        print("Object Deleted")
c1 = student_infoinit()
c1.printresults()
del c1        


# Q32. A machine learning model has the following scores:
#
# model_scores = {
#     "Linear Regression": 0.82,
#     "Decision Tree": 0.88,
#     "Random Forest": 0.94
# }
#
# Print the accuracy of Random Forest.
# Add a new entry for "Logistic Regression" with accuracy 0.90.
# Print the updated dictionary.

class model_scores_init(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.model_scores = {"Linear Regression": 0.82, "Decision Tree": 0.88, "Random Forest": 0.94}
        return self.model_scores
    def dictExamples(self):
        self.model_scores["Logistic Regression"] = 0.90
        return self.model_scores
    def printresults(self):
        print(f"Original Dictionary : {self.dictionaryinitialization()}")
        print(f"Accuracy of Random Forest : {self.dictionaryinitialization().get("Random Forest")}")
        print(f"Updated Dictionary : {self.dictExamples()}")
    def __del__(self):
        print(f"Object Deleted")

c1 = model_scores_init()
c1.dictionaryinitialization()
c1.dictExamples()
c1.printresults()
del c1

# Q33. A dataset has the following missing-value counts:
#
# missing_values = {
#     "age": 5,
#     "salary": 12,
#     "experience": 0,
#     "department": 8
# }
#
# Update the missing-value count for "salary" to 10.
# Remove the "experience" entry.
# Print the updated dictionary.

class missing_value_init(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.missing_values = {"age": 5, "salary": 12, "experience": 0, "department": 8}
        return self.missing_values
    def dictExamples(self):
        self.missing_values["salary"] = 10
        del self.missing_values["experience"]
        print(f"Update Dictionary : {self.missing_values}")
    def __del__(self):
        print("Object Deleted")    
c1 = missing_value_init()
c1.dictionaryinitialization()
c1.dictExamples()
del c1

# Q34. A machine learning project stores the following
# evaluation metrics:
#
# metrics = {
#     "accuracy": 0.91,
#     "precision": 0.88,
#     "recall": 0.85,
#     "f1_score": 0.86
# }
#
# Print all metric names and their values using a loop.
# Calculate and print the average of the four metric values.

class  evaluationmetrics_init(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.metrics = {"accuracy": 0.91, "precision": 0.88, "recall": 0.85, "f1_score": 0.86}
    def printresults(self):
        for key,value in self.metrics.items():
            print(f"Key : {key}") 
            print(f"Value : {value}")  
        average = lambda d: sum(d.values())/len(d) if d else 0
        print(f"Average : {average(self.metrics)}")
    def __del__(self):
        print(f"Object Deleted")    
c1 = evaluationmetrics_init()
c1.dictionaryinitialization()
c1.printresults()
del c1




# Q35. A dataset contains customer information:
#
# customers = {
#     "C101": 25000,
#     "C102": 45000,
#     "C103": 18000,
#     "C104": 60000,
#     "C105": 35000
# }
#
# The keys represent customer IDs, and the values represent
# their annual spending.
#
# Create a new dictionary containing only customers whose
# spending is greater than 30000.
# Print the filtered dictionary.

class customerspending(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.customers = {"C101": 25000, "C102": 45000, "C103": 18000, "C104": 60000, "C105": 35000}
    def dictExamples(self):
        dict = lambda x:{k: v for k, v in x.items() if v > 30000} if x else 0     
        print(f"{dict(self.customers)}")
    def __del__(self):
        print("Object Deleted")
c1 = customerspending()
c1.dictionaryinitialization()
c1.dictExamples()
del c1        


# Q36. A machine learning pipeline stores hyperparameters:
#
# hyperparameters = {
#     "learning_rate": 0.01,
#     "epochs": 100,
#     "batch_size": 32
# }
#
# Add a new hyperparameter named "optimizer" with value "Adam".
# Update the learning rate to 0.001.
# Print all keys and values using a loop.
# Check whether "dropout" exists in the dictionary.

class hyperparameters(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.hyperparameters = {"learning_rate": 0.01, "epochs": 100, "batch_size": 32}
    def dictExamples(self):
        self.hyperparameters["optimizer"] = "Adam"
        self.hyperparameters["learning_rate"] = 0.001
        for key, value in self.hyperparameters.items():
            print(f"key : {key}") 
            print(f"Value : {value}")
        if "dropout" in self.hyperparameters:
            print(f"Key Exists")
        else:
            print(f"Key Does not Exists")
    def __del__(self):
        print("Object Deleted")                   
c1 = hyperparameters()
c1.dictionaryinitialization()
c1.dictExamples()
del c1

# Q37. A data scientist stores the following model results:
#
# model_results = {
#     "Linear Regression": {"accuracy": 0.82, "f1_score": 0.80},
#     "Decision Tree": {"accuracy": 0.88, "f1_score": 0.86},
#     "Random Forest": {"accuracy": 0.94, "f1_score": 0.92}
# }
#
# Print the accuracy and F1-score of each model.
# Identify the model with the highest accuracy.
# Print its name and accuracy.

class model_results_init(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.model_results = { "Linear Regression": {"accuracy": 0.82, "f1_score": 0.80}, "Decision Tree": {"accuracy": 0.88, "f1_score": 0.86}, "Random Forest": {"accuracy": 0.94, "f1_score": 0.92} }
    def dictExamples(self):
        for modelname, metricname in self.model_results.items():
            print(f"Model Name : {modelname}" )
            for metricname, metric in metricname.items():
                print(f"MetricName : {metricname} the Score is : {metric}")
        highestaccuracymodel = max(self.model_results, key=lambda x: self.model_results[x]["accuracy"])
        print(f"{highestaccuracymodel} with highest accuracy : {self.model_results[highestaccuracymodel]["accuracy"]}")
    def __del__(self):
        print("Object Deleted")

c1 = model_results_init()
c1.dictionaryinitialization()
c1.dictExamples()
del c1                    


# Q38. A company tracks the number of customers in different
# age groups:
#
# age_groups = [25, 32, 28, 45, 32, 25, 40, 28, 32, 45]
#
# Create a dictionary that counts how many times each age
# appears in the list.
#
# Expected structure:
# {25: 2, 32: 3, ...}
#
# Solve this using a normal dictionary and a loop.
# Do not use Counter from the collections module.

class age_groups(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.age_groups = [25, 32, 28, 45, 32, 25, 40, 28, 32, 45]
    def dictExamples(self):
        i = 0
        age_group_count = {}
        while i<len(self.age_groups):
            j = 0
            count = 0
            while j<len(self.age_groups):
                if self.age_groups[i] == self.age_groups[j]:
                    count = count + 1
                    age_group_count[self.age_groups[i]] =  count
                else:
                    age_group_count[self.age_groups[i]] =  count  
                j = j + 1         
            i = i + 1
        print(f"{age_group_count}")
    def __del__(self):
        print("Object Deleted")    

c1 = age_groups()
c1.dictionaryinitialization()
c1.dictExamples()     
del c1   

        
# Q39. A dataset contains the following actual customer
# categories:
#
# actual_categories = ["A", "B", "A", "C", "B", "A", "C", "B"]
#
# Create a dictionary that counts the frequency of each
# category.
#
# Then calculate the percentage of records belonging to
# each category.
#
# Example:
# Category A: 37.5%
#
# Print both the counts and percentages.

class actual_customer_categories(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.actual_categories = ["A", "B", "A", "C", "B", "A", "C", "B"]
    def dictExamples(self):
        i = 0
        actual_categories_count = {}
        ucat = {}
        average = 0.00
        while i<len(self.actual_categories):
            j = 0
            count = 0
            while j<len(self.actual_categories):
                if self.actual_categories[i] == self.actual_categories[j]:
                    count = count + 1
                    actual_categories_count[self.actual_categories[i]] =  count
                else:
                    actual_categories_count[self.actual_categories[i]] =  count  
                j = j + 1         
            i = i + 1       
        print(f"{actual_categories_count}")

        for key, value in actual_categories_count.items():
            average = ((value)/len(self.actual_categories))*100
            print(f"Category {key} : {average}")
    def __del__(self):
        print("Object Deleted")    

c1 = actual_customer_categories()
c1.dictionaryinitialization()
c1.dictExamples()     
del c1   




# Q40. A data science team maintains two dictionaries
# containing model performance results:
#
# experiment_1 = {
#     "Linear Regression": 0.82,
#     "Decision Tree": 0.88,
#     "Random Forest": 0.94
# }
#
# experiment_2 = {
#     "Decision Tree": 0.90,
#     "Random Forest": 0.96,
#     "KNN": 0.85
# }
#
# Perform the following tasks:
#
# 1. Merge both dictionaries into a new dictionary.
# 2. If a model appears in both dictionaries, retain the
#    higher accuracy score.
# 3. Print the final dictionary.
# 4. Identify the model with the highest accuracy.
# 5. Print all models whose final accuracy is greater than 0.90.

class modelperformanceresults(Dictionariesimplementation):
    def dictionaryinitialization(self):
        self.experiment_1 = {"Linear Regression": 0.82, "Decision Tree": 0.88, "Random Forest": 0.94}
        self.experiment_2 = {"Decision Tree": 0.90, "Random Forest": 0.96, "KNN": 0.85}
    def dictExamples(self):
        mergedmodel = {}
        mergedmodel = self.experiment_1 | self.experiment_2
        print(f"{mergedmodel}")
        print(f"{max(mergedmodel,key=mergedmodel.get)} : {mergedmodel[max(mergedmodel,key=mergedmodel.get)]}")
        for key, value in mergedmodel.items():
            if value > 0.90:
                print(f"{key} : {value}")
    def __del__(self):
        print("Object Deleted")            

c1 = modelperformanceresults()
c1.dictionaryinitialization()
c1.dictExamples()
del c1
