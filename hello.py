#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style=background:orange><c><h1><i>College Life</i></c></h1><p>College life is known as one of the most memorable years of one’s life. It is entirely different from school life. College life exposes us to new experiences and things that we were not familiar with earlier. For some people, college life means enjoying life to the fullest and partying hard. While for others, it is time to get serious about their career and study thoroughly for a brighter future.</p></b><h1><b><i>The Transition from School Life to College Life</i></b></h1></b><p>College life is a big transition from school life. We go through a lot of changes when we enter college. Our schools were a safe place where we had grown up and spent half our lives. The transition to college is so sudden that you’re no longer protected by your teachers and friends of your school time.</p></b><p>College life poses a lot of challenges in front of you. You are now in a place full of unfamiliar faces where you need to mingle in. It teaches us to socialize and form opinions of our own. In college, students learn their free will and they go on to become more confident and composed.</p></b><p>In school life, we were always dependant on our friends or teachers. College life teaches us to be independent. It makes us stronger and teaches us to fight our own battles. It also makes us serious about our careers. We make decisions that will affect our future all by ourselves, as in school life our parents did it for us.</p></b><P>Additionally, in schools, we viewed our teachers as our mentors and sometimes even parents. We respected them and kept a distance. However, in college life, the teacher-student relationship becomes a bit informal. They become more or less like our friends and we share our troubles and happiness with them as we did with our friends.</p></b><h1>College Life Experience</h1></i></b><p>College life experience is truly one of a kind. The most common memories people have of college life are definitely goofing around with friends. They remember how the group of friends walked around the college in style and playing silly pranks on each other.Another college life experience I have seen people cherish the most is the annual fest. The annual fest created so much excitement and buzz amongst the students. Everyone welcomed other colleges with open arms and also made friends there. All the competitions were carried out in a good spirit and the students dressed their best to represent their college well.</p></b><h1><i><b>The Hardest Part of College Life</i></h1></b><p>As a college student, the hardest part of college life was leaving college after graduation or post-graduation. The last days of college were the hardest, knowing that soon you will be departing your friends, the campus, teachers and completely leaving behind a part of life.</p></div>"
if __name__=='__main__':
    app.run(debug=True)
