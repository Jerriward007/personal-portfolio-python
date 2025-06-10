class BioinformaticianProfile:
    def __init__(self):
        self.name = "Ogungbemi Jeremiah Kola"
        self.background = "Plant Biologist | Aspiring Bioinformatician | Data Scientist"
        self.education = "B.Sc. in Botany, Federal University of Agriculture, Abeokuta"
        self.skills = [
            "Python for Data Science",
            "R Programming",
            "HTML & CSS (Responsive Web Design)",
            "Basic Statistics and Research Methods",
            "Plant Physiology & Pathology",
            "Bioinformatics",
            "Computational Biology",
            "Currently learning JavaScript"
        ]
        self.projects = [
            "Medical Data Visualizer",
            "Sea Level Predictor",
            "Demographic Data Analyzer",
            "Mean-Variance-Standard Deviation Calculator",
            "Appreciation Message Page",
            "Estatiq Wears Survey Form",
            "Estatiq Wears Homepage",
            "Technical Documentation Site"
        ]
        self.other_roles = [
            "Fashion Designer",
            "Founder of Estatiq Wears"
        ]
        self.goals = (
            "To become a top-tier bioinformatician capable of using computational tools "
            "to interpret biological data, particularly in infectious diseases and genomics."
        )

    def introduction(self):
        return f"Hello, I'm {self.name}!"

    def summary(self):
        print(self.introduction())
        print("\n🎓 Education:")
        print(f" - {self.education}")

        print("\n🧠 Skills & Interests:")
        for skill in self.skills:
            print(f" - {skill}")

        print("\n💼 Projects:")
        for project in self.projects:
            print(f" - {project}")

        print("\n🧵 Other Roles:")
        for role in self.other_roles:
            print(f" - {role}")

        print("\n🎯 Career Goal:")
        print(f" - {self.goals}")


if __name__ == "__main__":
    profile = BioinformaticianProfile()
    profile.summary()
