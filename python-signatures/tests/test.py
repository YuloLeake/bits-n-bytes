from collections.abc import Callable
from inspect import iscoroutinefunction, signature
from typing import Optional

import pytest


def takes_keyword_arg(f: Callable, kwarg_key: str) -> bool:
    sig = signature(f)
    return kwarg_key in sig.parameters


def is_argument_type(
    f: Callable,
    arg_type: type,
    *,
    arg_idx: Optional[int] = None,
    kwarg_key: Optional[str] = None
) -> bool:
    idx_set = arg_idx is not None
    kwarg_set = kwarg_key is not None
    if idx_set and kwarg_set or not (idx_set or kwarg_set):
        raise Exception("Must be either arg_idx or kwarg_key.")

    params = signature(f).parameters
    if idx_set:
        arg = tuple(params.values())[arg_idx]
    else:
        arg = params[kwarg_key]
    return arg.annotation == arg_type


def is_async(f: Callable) -> bool:
    return iscoroutinefunction(f)


class Test_signature_check:

    def test_function_has_data2(self):
        # Given
        def func(data1, data2):
            pass

        # When-Then
        assert takes_keyword_arg(func, "data2")

    def test_function_does_not_have_data2(self):
        # Given
        def func(data1, data3):
            pass

        # When-Then
        assert not takes_keyword_arg(func, "data2")
        # assert takes_keyword_arg(func, "data2")

    def test_method_has_data2(self):
        # Given
        class A:
            def func(self, data1, data2):
                pass
        a = A()

        # When-Then
        assert takes_keyword_arg(a.func, "data2")

    def test_method_does_not_have_data3(self):
        # Given
        class A:
            def func(self, data1, data2):
                pass
        a = A()

        # When-Then
        assert not takes_keyword_arg(a.func, "data3")

    def test_first_func_pos_arg_is_integer_type(self):
        # Given
        def func(pos1: int, pos2: float, pos3: str, pos4: dict):
            pass

        # When-Then
        assert is_argument_type(func, int, arg_idx=0)

    def test_method_func_pos2_is_boolean_type(self):
        # Given
        def func(pos1: int, pos2: bool, pos3: str, pos4: dict):
            pass

        # When-Then
        assert is_argument_type(func, bool, kwarg_key="pos2")

    def test_first_method_pos_arg_is_integer_type(self):
        # Given
        class A:
            def func(self, pos1: int, pos2: float, pos3: str, pos4: dict):
                pass
        a = A()

        # When-Then
        assert is_argument_type(a.func, int, arg_idx=0)

    def test_method_kwarg_pos2_is_float_type(self):
        # Given
        class A:
            def func(self, pos1: int, pos2: float, pos3: str, pos4: dict):
                pass
        a = A()

        # When-Then
        assert is_argument_type(a.func, float, kwarg_key="pos2")

    def test_pos_idx_and_kwarg_key_cannot_be_set(self):
        # Given
        def func(pos1: str):
            pass

        # When-Then
        with pytest.raises(Exception):
            is_argument_type(func, str, arg_idx=0, kwarg_key="pos1")

    def test_pos_idx_and_kwarg_key_cannot_be_null(self):
        # Given
        def func(pos1: dict):
            pass

        # When-Then
        with pytest.raises(Exception):
            is_argument_type(func, dict)

class Test_concurrency_check:

    def test_function_is_sync(self):
        # Given
        def func():
            pass

        # When-Then
        assert not is_async(func)

    def test_method_is_sync(self):
        # Given
        class A:
            def method(self):
                pass

        a = A()

        # When-Then
        assert not is_async(a.method)

    def test_function_is_async(self):
        # Given
        async def afunc():
            pass

        # When-Then
        assert is_async(afunc)

    def test_method_is_async(self):
        # Given
        class A:
            async def amethod(self):
                pass

        a = A()

        # When-Then
        assert is_async(a.amethod)
