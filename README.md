# Client-Server-Development
CRUD file and creating a functional dashboard that run of CRUD  method

# CS 340 - Project Two  
## Grazioso Salvare MongoDB Dashboard  

### Project Summary
This project is a Python-based interactive dashboard that integrates with a MongoDB database to manage and visualize animal outcomes data from the Austin Animal Center (AAC). It builds upon the CRUD module created in Project One, extending its functionality into a client-friendly web application.  

The dashboard enables Grazioso Salvare to:  
- Apply **rescue-type filters** (Water Rescue, Mountain/Wilderness Rescue, Disaster/Individual Tracking).  
- Filter by **animal type** (Dog or Cat).  
- View results in a **dynamic DataTable** with sorting, filtering, and pagination.  
- Analyze breed distribution through a **real-time pie chart**.  
- Explore animal locations using an **interactive map** with tooltips and popups.  
- Access the application with **secure MongoDB authentication** through the CRUD module.  

By combining the database-driven CRUD operations with the visualization and interactivity of Dash, this project transforms raw AAC data into actionable insights. It improves usability, efficiency, and scalability—helping both technical and non-technical users at Grazioso Salvare make better decisions when planning rescue operations.  

---

## Reflections  

### How do you write programs that are maintainable, readable, and adaptable?  
I focused on writing modular, object-oriented code in the CRUD Python module from Project One. By encapsulating database operations (create, read, update, delete) into methods of a single class, the module was reusable and easy to connect to the dashboard in Project Two. This approach made it simpler to update functionality in one place without breaking other parts of the project. The advantage of working in this way is that the same CRUD module can now be reused in other applications, such as different dashboards or scripts, without rewriting database logic. This separation of concerns improves maintainability and adaptability as requirements change.  

### How do you approach a problem as a computer scientist?  
When approaching the requirements for the Grazioso Salvare project, I first broke down the client’s needs into smaller tasks such as loading the dataset, creating an authenticated user, implementing CRUD operations, and then connecting those operations to dashboard widgets. Compared to earlier assignments, this project required me to think more about system design and user experience, rather than only writing small, isolated programs. I relied on strategies such as incremental testing (verifying each CRUD method in Jupyter before integrating it) and modularization (separating database logic from dashboard logic). In future projects, I would continue using these strategies, while also leveraging indexing and aggregation pipelines in MongoDB to meet more advanced client queries efficiently.  

### What do computer scientists do, and why does it matter?  
Computer scientists solve problems by designing and implementing systems that manage data, automate processes, and make complex tasks easier for users. In this project, my work allows a company like Grazioso Salvare to filter and visualize animal data quickly, supporting decisions about rescue operations. This matters because efficient data systems directly improve how organizations perform their missions, saving time, reducing errors, and enabling better outcomes. For Grazioso Salvare, that could mean finding the right rescue dog faster, ultimately helping them save more lives.  
