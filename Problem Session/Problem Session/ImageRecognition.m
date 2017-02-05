//
//  ImageRecognition.m
//  Problem Session
//
//  Created by Chaitanya Ravuri on 2/5/17.
//  Copyright © 2017 Chaitu Ravuri. All rights reserved.
//

#import "ImageRecognition.h"

@implementation ImageRecognition
- (void)awakeFromNib
{
    NSString *pluginPath = [[NSBundle mainBundle] pathForResource:@"/Users/cravuri/Documents/harker/LSHacks/src/main/main.py"
                                                           ofType:@"plugin"];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    Class pyClass = [pluginBundle classNamed:@"answerSheet"];
    py = [[pyClass alloc] init];
}

- (void)dealloc
{
    [py release];
    [super dealloc];
}

- (void)printAlg
{
    return [py printAlg1ProblemSheet];
}

- (void)printComp
{
    return [py printCompetitionProblemSheet];
}
@end
