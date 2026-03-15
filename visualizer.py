import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
class DataVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
    def histplots(self,columns,titles, axis_x,n,m, main_title='Distribution of Continuous Variables'):
        sns.set_style('whitegrid')
        fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(15,10), squeeze=False)
        if main_title:
            fig.suptitle(main_title, fontsize=12)
        axes = axes.flatten()
        for i,(col, title,x) in enumerate(zip(columns, titles, axis_x)):
            sns.histplot(self.df[col], kde=True, bins=30, ax = axes[i])
            axes[i].set_title(title)
            axes[i].set_xlabel(x)
            axes[i].set_ylabel('Number of Apartments')
        for j in range(len(columns), n*m):
            axes[j].set_visible(False)
        plt.tight_layout()
        plt.show()
    def boxplots(self,columns,titles, axis_x):
        sns.set_style('whitegrid')
        for i,(col, title, x) in enumerate(zip(columns, titles, axis_x)):
            plt.figure(figsize=(14,3))
            sns.boxplot(x = self.df[col])
            plt.title(f"Boxplot for {title}")
            plt.xlabel(x)
            plt.show()
    def histplots_test(self,cluster,column, sup_title,n,m):
        fig, axes =  plt.subplots(nrows=n,ncols=m, figsize=(12,8))
        fig.suptitle(sup_title, fontsize=16)
        axes = axes.flatten()
        for i, city in enumerate(cluster):
            city_data = self.df[self.df['city'] == city]
            sns.histplot(data=city_data, x=column, kde=True, bins=30, ax=axes[i],color='teal')
            axes[i].set_title(city.capitalize())
            axes[i].set_ylabel("Number of Apartments")
            axes[i].set_xlabel("Price [PLN]")
        for j in range(len(cluster),n*m):
            axes[j].set_visible(False)
        plt.tight_layout()
        plt.show()
    def boxplots_test(self,cluster,column,sup_title, n,m):
        fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(12,8))
        fig.suptitle(sup_title, fontsize=16)
        axes = axes.flatten()
        for i, city in enumerate(cluster):
            city_data = self.df[self.df['city'] == city]
            sns.boxplot(data=city_data, x=column,ax=axes[i])
            axes[i].set_title(city.capitalize())
            axes[i].set_xlabel("Price [PLN]")
        for j in range(len(cluster), n*m):
            axes[j].set_visible(False)
        plt.tight_layout()
        plt.show()
    def countplots(self,columns,titles,y_label):
        for i, (col, title) in enumerate(zip(columns, titles)):
            plt.figure(figsize=(8,10))
            sns.countplot(data = self.df, x = col, order=self.df[col].value_counts().index,hue=col, palette='viridis',legend=False)
            plt.title(title)
            plt.ylabel(y_label)
            plt.xticks(rotation=45)
            plt.show()
    def barplots(self, col1,col2,title):
        plt.figure(figsize=(10,8))
        sns.barplot(data=self.df, x=col1, y=col2, palette='mako',hue=col1,legend=False)
        plt.title(title)
        plt.show()
    def heatmap(self):
        df_numeric = self.df.select_dtypes(include='number')
        correlations = df_numeric.corr()
        plt.figure(figsize=(12,10))
        sns.heatmap(correlations, cmap='inferno',annot=True, fmt='.2f',square=True)
        plt.show()
    def scatterplots(self, col1, col2,title):
        plt.figure(figsize=(15,10))
        sns.scatterplot(data=self.df, x=col1, y=col2,legend='auto')
        plt.title(title)
        plt.show()
    def lineplots(self,col1,col2,col_hue,palette,title,y_label,legend_title):
        plt.figure(figsize=(14,7))
        sns.lineplot(data= self.df, x=col1, y=col2,hue=col_hue, marker='o',linewidth=2,palette=palette)
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel('Date')
        plt.legend(title=legend_title, bbox_to_anchor=(1.05,1), loc='upper left')
        plt.tight_layout()
        plt.show()
    def bivariate_boxplot(self, col1, col2, title):
        plt.figure(figsize=(12,10))
        sns.boxplot(data=self.df, x=col1, y=col2, palette='Set2', hue=col1, legend=False)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    def scatterplot_test(self,pred,res):
        plt.figure(figsize=(12,10))
        plt.scatter(pred,res,alpha=0.1)
        plt.axhline(y=0, color='r', linestyle='--')
        plt.title('Residuals vs Predicted')
        plt.xlabel('Predicted Price')
        plt.ylabel('Residuals')
        plt.show()
    def probplot(self,res):
        plt.figure(figsize=(12,10))
        stats.probplot(res, dist='norm', plot=plt)
        plt.title('Normal Q-Q Plot')
        plt.show()