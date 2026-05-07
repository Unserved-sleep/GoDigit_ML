from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class CurriculumNode:
    id: int
    title: str
    type: str
    credits: float
    children: list[CurriculumNode] = field(default_factory=list)

    def add_child(self, node: CurriculumNode) -> None:
        self.children.append(node)

program  = CurriculumNode(1, 'B.Sc. Computer Science', 'program', credits=None)
cs101    = CurriculumNode(2, 'CS101 Intro to Programming', 'course', credits=3)
cs201    = CurriculumNode(3, 'CS201 Data Structures',      'course', credits=3)
mod1     = CurriculumNode(4, 'Module 1: Arrays & Lists',   'module', credits=None)
mod2     = CurriculumNode(5, 'Module 2: Trees & Graphs',   'module', credits=None)
lesson1  = CurriculumNode(6, 'Lesson 1: Binary Trees',     'lesson', credits=1)
lesson2  = CurriculumNode(7, 'Lesson 2: BST Operations',   'lesson', credits=1)

program.add_child(cs101)
program.add_child(cs201)
cs201.add_child(mod1)
cs201.add_child(mod2)
mod2.add_child(lesson1)
mod2.add_child(lesson2)


