from manim import *

class Try(Scene):
    def construct(self):
        c = Circle(fill_opacity=1)
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(c, s))
        self.wait()
        self.play(FadeOut(s))
        self.wait()
    
class trytwo(Scene):
    def construct(self):
        ax =Axes(x_range= (-5,5),y_range= (-5,5))
        def F(x):
            return (x-2)*x*(x+2)/2
        curve = ax.plot( F , color=PURE_RED)
        area = ax.get_area(curve,x_range=(-2,0))

        green_square = Square(color = GREEN, fill_opacity = 1)
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(FadeIn(area))
        self.play(DrawBorderThenFill(green_square))
        self.wait(2)
        UP

class trythree(Scene):
    def construct(self):
        s = Square(color = RED, fill_opacity = 0.5)
        c = Circle(color = BLUE , fill_opacity = 0.5)
        s.move_to([0,0,0],aligned_edge=UP+LEFT)
        self.add(c,s)
        # next_to
        # shift
        # align_to

from manim.utils.unit import Percent , Pixels

class tryfuce(Scene):
    def construct(self):
        for perc in range(5 , 51 ,5):
            self.add(Circle(radius= perc * Percent(X_AXIS)))

class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        yellow_dot = Dot(color=YELLOW).next_to(red_dot,RIGHT)
        dot_group = VGroup(red_dot,yellow_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2,color=RED_A) for _ in range(10)])
        circles.arrange(UP,buff=0.2)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW) for i in range(8)])
        stars.arrange_in_grid(2,4,buff=0.3)
        self.add(stars)

        t = Text("hello world!!!" , font_size= 50)
        self.add(t)

class BasicAnimation(Scene):
    def construct(self):
        ploys = VGroup(*[RegularPolygon(5 , radius = 1 , fill_opacity = 0.5 )for j in range(5)]).arrange(RIGHT)
        self.play(DrawBorderThenFill(ploys),run_time = 2)
        self.play(Rotate(ploys[0],PI,rate_func = lambda t:t),
            Rotate(ploys[1],PI,rate_func = smooth),
            Rotate(ploys[2],PI,rate_func = lambda t:np.sin(t*PI)),
            Rotate(ploys[3],PI,rate_func = there_and_back),
            Rotate(ploys[4],PI,rate_func = lambda t:t),
            run_time = 10
            # .scale(2) 扩大比例尺
        )
        self.wait()

class AnimateSyntax(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        self.add(s,c)

        self.play(s.animate.shift(UP) , c.animate.shift(DOWN))
        self.play(VGroup(s,c).animate.arrange(LEFT , buff=2))
        self.play(s.animate(rate_func = smooth).shift(RIGHT).scale(2))
        self.wait()