#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

static PyObject *
spam_random(PyObject *self, PyObject *args)
{
  int value = rand();
  return PyLong_FromLong(value);
}

static PyObject *
spam_list_random(PyObject *self, PyObject *args)
{
  unsigned int count = 0;
  if (!PyArg_ParseTuple(args, "I", &count))
    return NULL;

  PyObject *outputList = PyList_New(0);
  if (!outputList)
    return NULL;

  for (unsigned int i=0; i < count; i++) {
    PyList_Append(outputList, PyLong_FromLong(rand()));
  }

  return outputList;
}

static PyObject *
spam_fib(PyObject *self, PyObject *args)
{
  int n;
  if (!PyArg_ParseTuple(args, "i", &n))
    return NULL;

  // Write code here
  unsigned long y = 0;

  return PyLong_FromUnsignedLong(y);
}


static PyObject *
spam_system(PyObject *self, PyObject *args)
{
  const char *command;
  int sts;

  printf("Running A C Extensions :)\n");

  if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;
  sts = system(command);
  return PyLong_FromLong(sts);
}

static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    {"fib", spam_fib, METH_VARARGS,
      "calculate n fibonacci number"},
    {"rand", spam_random, METH_VARARGS,
      "returns a random int"},
    {"randlist", spam_list_random, METH_VARARGS,
      "returns a list of random numbers"},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    time_t t;
    srand((unsigned) time(&t));
    return PyModule_Create(&spammodule);
}
