//
//  CameraViewController.h
//  Problem Session
//
//  Created by Chaitanya Ravuri on 2/4/17.
//  Copyright © 2017 Chaitu Ravuri. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CameraViewController : UIViewController <UIImagePickerControllerDelegate, UINavigationControllerDelegate>
@property (strong, nonatomic) IBOutlet UIImageView *imageView;
- (IBAction)takePhoto;
- (IBAction)selectPhoto;

@end
