#define PY_MAJOR_VERSION 3
#undef ENABLE_PYTHON_MODULE
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/builtins/None.hpp>
#include <pythonic/include/builtins/print.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/builtins/None.hpp>
#include <pythonic/builtins/print.hpp>
#include <pythonic/types/str.hpp>
namespace 
{
  namespace __pythran_demo6
  {
    struct foo
    {
      typedef void callable;
      ;
      struct type
      {
        typedef pythonic::types::none_type __type0;
        typedef typename pythonic::returnable<__type0>::type __type1;
        typedef __type1 result_type;
      }  ;
      inline
      typename type::result_type operator()() const;
      ;
    }  ;
    struct msg
    {
      typedef void callable;
      typedef void pure;
      struct type
      {
        typedef pythonic::types::str __type0;
        typedef typename pythonic::returnable<__type0>::type __type1;
        typedef __type1 result_type;
      }  ;
      inline
      typename type::result_type operator()() const;
      ;
    }  ;
    inline
    typename foo::type::result_type foo::operator()() const
    {
      pythonic::builtins::functor::print{}(pythonic::types::str("hello pythran"));
      return pythonic::builtins::None;
    }
    inline
    typename msg::type::result_type msg::operator()() const
    {
      {
        static typename msg::type::result_type tmp_global = pythonic::types::str("hello pythran");
        return tmp_global;
      }
    }
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
inline
typename __pythran_demo6::foo::type::result_type foo0() 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_demo6::foo()();
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}

static PyObject *
__pythran_wrap_foo0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[0+1];
    (void)args_obj;
    char const* keywords[] = { nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "",
                                     (char**)keywords ))
        return nullptr;
    if(1)
        return to_python(foo0());
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_foo(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_foo0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "foo", "\n""    - foo()", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "foo",
    (PyCFunction)__pythran_wrapall_foo,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n""\n""    - foo()"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "demo6",            /* m_name */
  "",         /* m_doc */
  -1,                  /* m_size */
  Methods,             /* m_methods */
  NULL,                /* m_reload */
  NULL,                /* m_traverse */
  NULL,                /* m_clear */
  NULL,                /* m_free */
};
PyMODINIT_FUNC
PyInit_demo6(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
#if defined(GNUC) && !defined(__clang__)
__attribute__ ((externally_visible))
#endif
#endif
;
PyMODINIT_FUNC
PyInit_demo6(void) {
    import_array();

    PyObject* theModule = PyModule_Create(&moduledef);
    if(! theModule)
        return theModule;

                #ifdef Py_GIL_DISABLED
                    PyUnstable_Module_SetGIL(theModule, Py_MOD_GIL_NOT_USED);
                #endif
    PyObject * theDoc = Py_BuildValue("(ss)",
                                      "0.18.0",
                                      "41737ace6d0e0870f9575adf73c5fc85a206f529bb6aef9fa9be4c0e3a935346");
    if(! theDoc)
        return theModule;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);

    PyModule_AddObject(theModule, "msg", to_python(__pythran_demo6::msg()()));
    return theModule;
}

#endif