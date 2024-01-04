## 0x03. Unittests and Integration Tests
### Unit Testing

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. A unit test is designed to evaluate standard inputs and corner cases. It should focus on testing the internal logic of the function being tested. Most calls to additional functions, especially those making network or database calls, should be mocked.

The primary goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

### Integration Testing

Integration tests aim to test a code path end-to-end. Typically, only low-level functions that make external calls, such as HTTP requests, file I/O, database I/O, etc., are mocked. Integration tests provide coverage for interactions between every part of your code.

To execute your tests, use the following command:

```bash
$ python -m unittest path/to/test_file.py
```
