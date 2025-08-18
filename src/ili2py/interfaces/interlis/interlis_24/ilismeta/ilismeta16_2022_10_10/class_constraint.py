from dataclasses import dataclass

from ili2py.interfaces.interlis.interlis_24.ilismeta.ilismeta16_2022_10_10.class_constraint_type import ClassConstraintType

__NAMESPACE__ = "http://www.interlis.ch/xtf/2.4/IlisMeta16"


@dataclass
class ClassConstraint(ClassConstraintType):
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/IlisMeta16"
