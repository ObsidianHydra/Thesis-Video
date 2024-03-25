from manim import *

class Title(Scene):
    def construct(self):
        first_image = ImageMobject("images/NIP Logo.png").shift(2*LEFT+2.5*UP) # instantiate the first image
        first_image.height = 2
        second_image = ImageMobject("images/SAND Logo.png").shift(2*RIGHT+2.5*UP) # instantiate the second image and position it relative to the first one
        second_image.height = 2
        self.play(FadeIn(first_image), FadeIn(second_image), run_time = 0.5)

        c = Rectangle(color = RED_A, height = 2.5, width = 9.0,fill_opacity = 0.1)

        self.play(DrawBorderThenFill(c), run_time = 0.75)

        title1 = Text("Variational Quantum Eigensolver", font_size = 40, slant="ITALIC").shift(UP * 0.6)
        title2 = Text("implemented on a", font_size = 40, slant = "ITALIC")
        title3 = Text("1D Quantum Harmonic Oscillator", font_size = 40, slant="ITALIC").shift(DOWN*0.6)
        self.play(Write(title1), Write(title2), Write(title3), run_time = 1)

        my_image = ImageMobject("images/dp.png").shift(2.6*DOWN + 1.4*LEFT) # instantiate the second image and position it relative to the first one
        my_image.height = 1.5

        bio1 = Text("John Samuel Suico", font_size = 20).shift(DOWN *2.2 + RIGHT)
        bio2 = Text("BS Physics", font_size = 15).shift(DOWN*2.5 + RIGHT)
        bio3 = Text("Adviser: Dr. Ronald Banzon", font_size = 15).shift(DOWN*2.7 + RIGHT)

        bio2.align_to(bio1,LEFT)
        bio3.align_to(bio2,LEFT)
        self.play(FadeIn(my_image), Write(bio1), Write(bio2), Write(bio3), run_time = 0.5)

        self.wait(3)

class QuantumComputing(Scene):
    def construct(self):
        title1 = Text("Quantum Computers", font_size = 40, color = "BLUE").shift(UP * 3)
        self.play(Write(title1), run_time = 1)

        c = Circle(radius = 2.0, color = WHITE, fill_opacity = 0.3)
        ellipse = DashedVMobject(Ellipse(width=4.0, height=1.0, color=WHITE),
                             num_dashes=20, dashed_ratio=0.5, dash_offset=0, color=WHITE, equal_lengths=True)
        self.play(DrawBorderThenFill(c), run_time = 1)
        self.play(Create(ellipse), run_time = 0.3)

        ket0 = Dot(color=WHITE).move_to([0, 2, 0]).scale(1)
        ket1 = Dot(color=WHITE).move_to([0, -2, 0]).scale(1)
        ket0_text = Tex(r"$\left|0\right>$").scale(0.5).next_to(ket0, UP).set_color(WHITE)
        ket1_text = Tex(r"$\left|1\right>$").scale(0.5).next_to(ket1, DOWN).set_color(WHITE)

        self.play(Create(ket0),Create(ket1),Create(ket0_text),Create(ket1_text), run_time = 0.3)

        blochsphere = VGroup(c,ellipse,ket0,ket1,ket0_text,ket1_text)
        
        self.wait(3)

        #Quantum computers offer a different paradigm of processing information using the principles of quantum mechanics.

        Psi = Tex(r"$\Psi = $")
        alpha = Tex(r"$ \alpha$")
        beta = Tex(r"$\beta$")
        plus = Tex("+")

        alpha.next_to(Psi,RIGHT)

        self.play(blochsphere.animate.scale(0.7).shift(3.5*LEFT), run_time = 0.8)  
        
        ket0_texteq = ket0_text.copy()
        ket1_texteq = ket1_text.copy()

        self.play(Write(Psi),Write(alpha),ket0_texteq.animate.scale(2).next_to(alpha))
        plus.next_to(ket0_texteq, RIGHT)
        beta.next_to(plus,RIGHT)
        self.play(Write(plus),Write(beta),ket1_texteq.animate.scale(2).next_to(beta))

        genqubit = VGroup(Psi,alpha,ket0_texteq,plus,beta,ket1_texteq)
        qubit = Text("Qubit", font_size = 40).next_to(genqubit,UP)
        self.play(Write(qubit),run_time=0.5)
        
        qubitgroup = VGroup(genqubit,qubit)

        self.wait(0.5)
        self.play(Indicate(beta),Indicate(alpha),Indicate(plus),run_time=0.5)
        self.wait(0.5)
        self.play(Indicate(ket0_texteq),run_time=0.5)
        self.play(Indicate(ket1_texteq),run_time=0.5)
        
        #The smallest unit of information in this paradigm is known as a qubit, which exists in a superposition of binary states ket 0 and ket 1.

        self.play(qubitgroup.animate.shift(UP*0.8),blochsphere.animate.shift(UP*0.8),run_time=0.5)

        bit = Text("Classical Bit", font_size = 40).next_to(qubitgroup,DOWN*4)

        self.play(Write(bit),run_time = 0.5)
        self.wait(0.5)
        zero = Tex("0", font_size = 40)
        mid = Tex(" or ", font_size = 40).next_to(zero)
        one = Tex("1", font_size = 40).next_to(mid)
        bittext = VGroup(zero,mid,one).next_to(bit,2*DOWN)
        
        self.play(Write(bittext),run_time = 0.8)
        self.wait(0.5)
        self.play(Indicate(zero),run_time=0.5)
        self.play(Indicate(one),run_time=0.5)
        self.wait(0.5)

        #As opposed to a classical bit which can only be in either state 0 or state 1.
        animations = []
        for mobject in self.mobjects:
            if mobject != title1:
                animations.append(FadeOut(mobject))
        self.play(*animations)

        top = Tex(r"$n$ qubits", font_size = 40).shift(UP)
        mid = Tex(r"access to", font_size = 40)
        bot = Tex(r"$2^n$ bits of information", font_size = 40).shift(DOWN)
        self.play(Write(top), run_time = 0.5)
        self.play(Write(mid), run_time = 0.5)
        self.play(Write(bot), run_time = 0.5)
        end_text1 = VGroup(top,mid,bot)

        self.play(end_text1.animate.shift(LEFT*3.5), run_time = 0.5)

        top2 = Tex(r"new methods", font_size = 40).shift(UP)
        mid2 = Tex(r"to tackle", font_size = 40)
        bot2 = Tex(r"computationally hard problems", font_size = 40).shift(DOWN)
        end_text2 = VGroup(top2,mid2,bot2)
        self.play(Write(top2),Write(mid2),Write(bot2), end_text2.animate.shift(RIGHT*3.5), run_time = 0.5)

        self.wait(3)

class VQE(Scene):
    def construct(self):
        title1 = Text("Variational Quantum Eigensolver", font_size = 40, color = "BLUE").shift(UP * 3)

        title2 = Text("VQE", font_size = 40, color = "BLUE").shift(UP * 3)
        title3 = Text("Single Particle 1D Harmonic Oscillator", font_size = 30, color = "WHITE").shift(UP * 2.2)

        self.play(Write(title1), run_time = 1)
        self.wait(2.75)
        self.play(Transform(title1,title2), run_time = 0.5)
        self.wait(0.75)

        varp = Tex(r"$E_0 \leq \frac{\left<\Psi\left|\hat{H}\right|\Psi\right>}{\left<\Psi|\Psi\right>}$")
        self.play(Write(varp), run_time = 0.5)
        self.play(varp.animate.shift(RIGHT*2), run_time = 0.5)
        varptext1 = Text(r"Variational", font_size = 40).shift(UP*0.5 + LEFT*2)
        varptext2 = Text(r"Principle", font_size = 40).shift(DOWN*0.5 + LEFT*2)
        self.play(Write(varptext1),Write(varptext2), run_time = 0.5)
        self.wait(2)

        animations = []
        for mobject in self.mobjects:
            if mobject != title1:
                animations.append(FadeOut(mobject))
        self.play(*animations)

        #We consider a particular hybrid algorithm known as the Variational Quantum Eigensolver, or VQE, which minimizes the energy of a system using the variational principle of quantum mechanics.

        self.play(Write(title3), run_time = 0.25)

        Ham1 = Tex(r"$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 x^2$",font_size = 50).shift(4*LEFT+UP)
        orH = Tex(r"or",font_size = 50).shift(4*LEFT+1.5*UP).next_to(Ham1,DOWN)
        Ham2 = Tex(r"$\hat{H} = \hbar\omega\left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2}\right)$",font_size = 50).shift(4*LEFT+UP).next_to(orH,DOWN)
        self.play(Write(Ham1), Write(orH), Write(Ham2), run_time = 0.5)

        where = Tex(r"where ", font_size = 30)
        where1l = Tex(r"$m$", font_size = 30).next_to(where)
        where1lins = Tex(r"$\hbar$", font_size = 30).next_to(where1l, DOWN)
        where2l = Tex(r"$\omega$", font_size = 30).next_to(where1lins, DOWN)
        where3l = Tex(r"$\hat{p}$", font_size = 30).next_to(where2l, DOWN)
        where4l = Tex(r"$\hat{x}$", font_size = 30).next_to(where3l, DOWN)
        where5l = Tex(r"$\hat{a}_{\pm}$", font_size = 30).next_to(where4l, DOWN)
        eq1 = Tex(r" = ", font_size = 30).next_to(where1l)
        eq1ins = Tex(r" = ", font_size = 30).next_to(where1lins)
        eq2 = Tex(r" = ", font_size = 30).next_to(where2l)
        eq3 = Tex(r" = ", font_size = 30).next_to(where3l)
        eq4 = Tex(r" = ", font_size = 30).next_to(where4l)
        eq5 = Tex(r" = ", font_size = 30).next_to(where5l)
        where1r = Tex(r"particle mass", font_size = 30).next_to(eq1)
        where1rins = Tex(r"reduced Planck's constant", font_size = 30).next_to(eq1ins)
        where2r = Tex(r"angular frequency", font_size = 30).next_to(eq2)
        where3r = Tex(r"momentum operator", font_size = 30).next_to(eq3)
        where4r = Tex(r"position operator", font_size = 30).next_to(eq4)
        where5r = Tex(r"ladder operators", font_size = 30).next_to(eq5)
        eq1ins.align_to(eq1,LEFT)
        eq2.align_to(eq1ins,LEFT)
        eq3.align_to(eq2,LEFT)
        eq4.align_to(eq3,LEFT)
        eq5.align_to(eq4,LEFT)

        wheregroup = VGroup(where,where1l,where1lins,where2l,where3l,where4l,where5l,
                            eq1,eq1ins,eq2,eq3,eq4,eq5,
                            where1r,where1rins, where2r,where3r,where4r,where5r).shift(6*LEFT+1.25*DOWN)
        self.play(Write(wheregroup),run_time = 1)

        self.wait(2)

        ax = Axes(x_range = [-5,5,1], y_range = [-1,5,1])
        labels = ax.get_axis_labels(
            Tex(r"$x$").scale(1.1), Tex(r"$V(x)$").scale(1.1)
        )

        f1 = ax.plot(lambda x: (1/5)*(x**2), color = BLUE)
        myplot = VGroup(ax,labels,f1).scale(0.5).shift(3*RIGHT,DOWN)
        self.play(Write(ax),Write(f1),Write(labels))

        self.wait(2)

        #We study a single particle 1D Harmonic Oscillator, which models the physics of a particle in a parabolic potential trap.

        Ham1disc = Tex(r"$\hat{H} = \frac{\hat{P}^2}{2m} + \frac{1}{2}m\omega^2 \hat{X}^2$",font_size = 50).shift(4*LEFT)
        orHdisc = Tex(r"or",font_size = 50).shift(4*LEFT+1.5*UP).next_to(Ham1disc,DOWN)
        Ham2disc = Tex(r"$\hat{H} = \hbar\omega\left(\hat{A}_{\pm}\hat{A}_{\mp} \pm \frac{1}{2}\right)$",font_size = 50).next_to(orHdisc,DOWN)
        newlabels = ax.get_axis_labels(
            Tex(r"$\left<i|\hat{X}|i\right>$").scale(1.1), Tex(r"$\frac{1}{2}m\omega^2\left<i|\hat{X}|i\right>^2$").scale(1.1)
        )
        axnew = Axes(x_range = [-5,5,1], y_range = [-1,5,1], tips = False).scale(0.5).move_to(ax)
        
        x = range(-5,6,1)
        y = [(1/5)*(i**2) for i in x]
        plot = axnew.plot_line_graph(x,y, vertex_dot_style=dict(color = BLUE))

        self.play(ReplacementTransform(Ham1,Ham1disc), ReplacementTransform(orH,orHdisc), ReplacementTransform(Ham2,Ham2disc), FadeOut(wheregroup),
                  Transform(labels,newlabels), Transform(ax,axnew), FadeOut(f1), Write(plot["vertex_dots"]), run_time = 0.5)
        self.wait(3)
        
        Ham1disc1 = Tex(r"$\hat{H} = \frac{\hat{P}^2}{2} +\frac{\hat{X}^2}{2}$",font_size = 50).shift(4*LEFT)
        orHdisc1 = Tex(r"or",font_size = 50).shift(4*LEFT+1.5*UP).next_to(Ham1,DOWN)
        Ham2disc1 = Tex(r"$\hat{H} = \hat{A}_{\pm}\hat{A}_{\mp} \pm \frac{I}{2}$",font_size = 50).shift(4*LEFT+UP).next_to(orH,DOWN)
        newlabels1 = ax.get_axis_labels(
            Tex(r"$\left<i|\hat{X}|i\right>$").scale(1.1), Tex(r"$\frac{\vphantom{>}^{\hphantom{2}}\left<i|\hat{X}|i\right>^2}{2}$").scale(1.1)
        )
        self.play(ReplacementTransform(Ham1disc,Ham1disc1), ReplacementTransform(orHdisc,orHdisc1), ReplacementTransform(Ham2disc,Ham2disc1),
                  Transform(labels,newlabels1),run_time = 0.5)
    
        self.wait(2)

        axnew1 = Axes(x_range = [-10,10,1], y_range = [-1,20,1], tips = False).scale(0.5).move_to(ax)
        axnew2 = Axes(x_range = [-2,2,1], y_range = [-1,0.8,1], tips = False).scale(0.5).move_to(ax) 
        
        x1 = range(-10,11,1)
        y1 = [(1/5)*(i**2) for i in x1]

        x2 = range(-2,3,1)
        y2 = [(1/5)*(i**2) for i in x2]

        f1new1 = axnew1.plot_line_graph(x1,y1, vertex_dot_style=dict(color = BLUE))
        f1new2 = axnew2.plot_line_graph(x2,y2, vertex_dot_style=dict(color = BLUE))
        self.play(Transform(ax,axnew1),FadeOut(plot["vertex_dots"]),Write(f1new1["vertex_dots"]),run_time = 1.5)
        self.wait(1)
        self.play(Transform(ax,axnew2),FadeOut(f1new1["vertex_dots"]),Write(f1new2["vertex_dots"]),run_time = 1.5)
        self.wait(2)

        #Line 7: To work on a quantum computer, we discretize the operators, representing them as matrices, and set \hbar,\omega,m to 1.
        #The position operator represents a lattice of points with arbitrary precision determining the size of the matrix and accuracy of the approximation.

        animations = []
        for mobject in self.mobjects:
            if mobject != title1:
                animations.append(FadeOut(mobject))
        self.play(*animations)
        
        decomp = Tex(r"$\hat{H} = \sum_{i = 1}^\mathcal{P} w_i \hat{S}_i$",font_size = 60).shift(LEFT*3)
        self.play(Write(decomp),run_time = 0.3)
        self.wait(1)
        strings = Tex(r"$, \hat{S}_i \in \{\sigma_x,\sigma_y,\sigma_z,I\}^{\otimes N}$",font_size = 60).shift(RIGHT*3)
        self.play(Write(strings),run_time = 0.3)
        self.wait(4)
        self.play(FadeOut(strings), FadeOut(decomp), run_time =0.3)
        
        #To measure this on a quantum computer, the Hamiltonian is written as a weighted sum of Pauli strings, or tensor products of Pauli and Identity matrices

        measure = Tex(r"$E_\text{VQE} = \min_{\boldsymbol{\theta}} \sum_{i = 1}^\mathcal{P}w_i\left<\mathbf{0}|U^\dagger(\boldsymbol{\theta})\hat{S}_iU(\boldsymbol{\theta})|\mathbf{0}\right>$", font_size = 55)
        self.play(Write(measure), run_time = 0.5)
        self.wait(4)
        self.play(measure.animate.shift(UP*1.5), run_time = 0.5)
        ansatz = Tex(r"$U(\boldsymbol{\theta})\left|\mathbf{0}\right>$", font_size = 60).shift(LEFT*4+DOWN)
        arrow = Arrow(start=LEFT*3, end=LEFT, buff = 0).next_to(ansatz)
        ex = Text("example", font_size = 30).next_to(arrow,UP)
        ansatzpic = ImageMobject("images/Ansatz.png").next_to(arrow,1.5*RIGHT)
        ansatzpic.height = 1.8
        self.play(Write(ansatz), Write(ex),Create(arrow),FadeIn(ansatzpic),  run_time = 0.5)
        self.wait(2)
        
        #The Pauli strings are then measured over a parameterized ansatz, which is a quantum circuit composed of rotational and entangling gates. 

        animations = []
        for mobject in self.mobjects:
            if mobject != title1:
                animations.append(FadeOut(mobject))
        self.play(*animations)

        import numpy as np
        term1 = Tex(r"$\left<\Psi(\boldsymbol{\theta})|\sigma_z \otimes \sigma_z\Psi(\boldsymbol{\theta})\right>$", font_size = 40)
        self.wait()
        p1 = Tex(r"$+1$", font_size=25)
        p2 = Tex(r"$-1$", font_size=25)
        self.play(Write(term1))

        rightdict = {}
        leftdict = {}
        pluses = []
        for i in range(0,3):
            for j in range(0,3):
                plus = []
                if(np.random.randint(0, 2) == 0):
                    test = p1.copy()
                    rightdict["key"+str(i)+str(j)] = 1
                else:
                    test = p2.copy() 
                    rightdict["key"+str(i)+str(j)] = -1
                if(np.random.randint(0, 2) == 0):
                    test2 = p1.copy()
                    leftdict["key"+str(i)+str(j)] = 1 
                else:
                    test2 = p2.copy()
                    leftdict["key"+str(i)+str(j)] = -1
                lcopy = term1.copy()
                rcopy = term1.copy()
                self.play(ReplacementTransform(rcopy, test),ReplacementTransform(lcopy, test2), test.animate.shift(UP+2.5*RIGHT+j*DOWN+i*RIGHT),test2.animate.shift(UP+2.5*LEFT+j*DOWN+i*LEFT), run_time = 0.2)
                plus.append(test)
                plus.append(test2)
                pluses.append(plus)
        self.wait(1)

        tobrace = []
        counter = 0
        for i in range(0,3):
            for j in range(0,3):
                self.play(pluses[counter][0].animate.move_to(LEFT+2*DOWN+3*LEFT + RIGHT*counter), pluses[counter][1].animate.move_to(LEFT+2*DOWN+3*LEFT + RIGHT*counter), run_time = 0.11)
                if leftdict["key"+str(i)+str(j)]*rightdict["key"+str(i)+str(j)] < 0:  
                    replace = p2.copy().move_to(pluses[counter][0])
                else:
                    replace = p1.copy().move_to(pluses[counter][0])
                self.play(Write(replace), FadeOut(pluses[counter][0]), FadeOut(pluses[counter][1]), run_time = 0.11)
                tobrace.append(replace)
                counter += 1
        self.wait(1)
        bracketgroup = VGroup(*tobrace)
        bracket = Brace(bracketgroup,UP)
        Ave = Text("Averaged", font_size = 30).next_to(bracket,UP)
        self.play(Write(bracket), Write(Ave), run_time = 0.3)
        self.wait(2)

        #Each term in the Pauli string is measured separately over each qubit in the Ansatz, and the eigenvalues are multiplied together and averaged over many repetitions of this process.

        animations = []
        for mobject in self.mobjects:
            if mobject != title1:
                animations.append(FadeOut(mobject))
        self.play(*animations)

        self.play(Write(measure.center()))
        self.wait(2)
        #The summation is then carried out in a classical computer, and the parameters are optimized in each iteration so as to arrive at the ground state energy.


class Test(Scene):
    def construct(self):
        ax = Axes(x_range = [-5,5,1], y_range = [-1,5,1])
        labels = ax.get_axis_labels(
            Tex(r"$x$").scale(1.1), Tex(r"$V(x)$").scale(1.1)
        )
        
        f1 = ax.plot(lambda x: (1/5)*(x**2), color = BLUE)

        x = range(-5,6,1)
        y = [(1/5)*(i**2) for i in x]
        plot = ax.plot_line_graph(x,y, vertex_dot_style=dict(color = BLUE))
        
        self.play(Write(ax),Write(labels), Write (f1))

        self.wait(2)

        self.play(FadeOut(f1),Write(plot["vertex_dots"]))
        self.wait(2)
        

        #We study a single particle 1D Harmonic Oscillator, which models the physics of a particle in a parabolic potential trap.
        
class Results(Scene):
    def construct(self):
        title1 = Text("Results", font_size = 40, color = "BLUE").shift(UP * 3)
        self.play(Write(title1), run_time = 0.3)

        TwoqHEA = ImageMobject("images/2qHEAresults.png").shift(3*LEFT)
        TwoqHEA.height = 3.5
        TwoqHEAansatz = ImageMobject("images/2qHEAansatz.png").next_to(TwoqHEA, RIGHT*1.5)
        TwoqHEAansatz.height = 1.8
        text1 = Text("Two Qubit HEA Ansatz", font_size = 40).shift(2.2*DOWN)

        TwoqUA = ImageMobject("images/2qunivresults.png").shift(3*LEFT)
        TwoqUA.height = 3.5
        TwoqUAansatz = ImageMobject("images/2qubitUniv.png").next_to(TwoqUA, RIGHT*1.5)
        TwoqUAansatz.height = 1.8
        text2 = Text("Two Qubit Universal Ansatz", font_size = 50).shift(2.2*DOWN)

        FourqHEA = ImageMobject("images/4qHEA.png").shift(3*LEFT)
        FourqHEA.height = 3.5
        FourqHEAansatz = ImageMobject("images/4qubitHEA.png").next_to(FourqHEA, RIGHT)
        FourqHEAansatz.height = 1.8
        text3 = Text("Four Qubit Ansatz", font_size = 50).shift(2.2*DOWN)

        myRes = [TwoqHEA, TwoqUA, FourqHEA]
        myAnsatz = [TwoqHEAansatz, TwoqUAansatz, FourqHEAansatz]
        mytext = [text1,text2,text3]

        for i in range(0,3):
            self.play(FadeIn(myRes[i]),FadeIn(mytext[i]),FadeIn(myAnsatz[i]), run_time = 0.5)
            self.wait(2.5)
            self.play(FadeOut(myRes[i]),FadeOut(mytext[i]), FadeOut(myAnsatz[i]), run_time = 0.5)
        #The results show that the VQE Pipeline successfully minimized the Hamiltonian,
        #except for the position basis Hamiltonian in the 4 Qubit Ansatz which struggled to converge.

        
        tq = Text("Two Qubit", font_size = 25)
        fq = Text("Four Qubit", font_size = 25)
        a1 = Text("HEA Ansatz", font_size = 25)
        a2 = Text("Universal Ansatz", font_size = 25)
        a3 = Text("Ansatz", font_size = 25)
        firstset = [tq,tq.copy(),fq]
        secondset = [a1,a2,a3]

        for i in range(0,3):
            myRes[i].height = 2.5
        self.play(FadeIn(myRes[0].move_to(LEFT*3)), FadeIn(myRes[1].center()), FadeIn(myRes[2].move_to(RIGHT*3)), run_time = 0.5)
        anims = []
        for i in range(0,3):
            firstset[i].next_to(myRes[i],DOWN)
            secondset[i].next_to(firstset[i],DOWN)
            anims.append(Write(firstset[i]))    
            anims.append(Write(secondset[i]))
        self.play(*anims, run_time = 0.5)
        self.wait(5)

def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    scene.play(*animations)

class FullScene(Scene):
    def construct(self):
        scenes = [Title,QuantumComputing,VQE,Results] #TODO: Add scenes here
        for scene in scenes:
            scene.construct(self)
            fade_out(self)