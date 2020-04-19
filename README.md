# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
    - Well, firstly in responding I would ask for clarification on whether the question is addressing the array Python data type with things being done to it, which might be a dynamic array, or dynamic arrays as in singly and doubly linked lists are dynamic arrays by definition. 
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
    -If we are talking a conventional python array, we can expect O(1) access of items, but O(n) for search, insertion and deletion. If we are talking a dynamic array that is a singly or doubly linked list, our access and search are O(n), but our insertion and deletion times are O(1).
* What is the worse case scenario if you try to extend the storage size of a dynamic array?
    - In the case of the contiguous python array, if the computer cannot extend the storage, appending to your current block of memory to a satisfactory degree, and the computer must instantiate and allocate a new, bigger block of memory, and assuming that is available, copy the entire array and all of the items into it.  In the case of a singly or doubly linked list, the blocks of memory do not have to be contiguous and therefore the worst case is that you fill your computer's memory completely to the brim with dynamic array linked list entries then you may have to delete other files to free up some space on your computer or buy more storage to continue extending the size of your array.

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
    - Blocks in a block chain are constructed from a genesis block.  A blockchain is technically a class/object, and the blocks are metaphorical, each block is a representation of the blockchain up to a certain point.  A block is an object made up of an index, a proof, and a previous hash, but might also include data like a transaction ledger and a timestamp of when the block was made.  Each block in the chain points forwards, as it is represented in the "previous_hash" of the next block, but also points backwards, containing the previous hash of the block before it.  By the way hashes work, this preserves the integrity of the data in the blockchain. 
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
    - A proof of work function is a function that takes in the last block on the chain, appends it with a number, and hashes it until the string of the last block in the chain appended with the proof number creates a hash below a certain amount(or in our case with a certain number of leading zeroes).  Then this number is returned to the Blockchain control server with the userId of the miner who found the lucky number, a block is mined and the reward is rewarded.  The only way to obtain a valid proof and mine a block is to guess and check against the last block in the chain, which was mined however much time ago.  Any attacker attempting to manipulate the blockchain, the data stored therein, or change the blocks would have to fight an unsustainable fight of staying as the longest chain in all the mined chains would otherwise disregard the shorter chain.
    - Fraud is impossible as you cannot manipulate the blockchain or its values without creating hashes that are completely different from what they should be, and is mathematically impossible to manipulate, say, the bitcoin blockchain into giving you thousands of bitcoin.

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least 16 coins.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least 20 times in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine at least 16 coins before the end of lunch.                                                               | The student was able to mine at least 16 coins before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 1000 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |

## Grading
The grade for this sprint challenge is the average of the number of points received (points/15)
