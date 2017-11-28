


#import <UIKit/UIKit.h>
#import "SelectableRoundView.h"
#import "CDZoomView.h"

@interface CDOverlayView : UIView<SelectabeRoundDelegate>{
    
    CDZoomView* _zoomView;

    SelectableRoundView* _topLeftCornerView;
    SelectableRoundView* _topRightCornerView;
    SelectableRoundView* _bottomLeftCornerView;
    SelectableRoundView* _bottomRightCornerView;
    
}

@property(nonatomic) CGPoint topLeftPath;
@property(nonatomic) CGPoint topRightPath;
@property(nonatomic) CGPoint bottomLeftPath;
@property(nonatomic) CGPoint bottomRightPath;

@property(nonatomic) CGFloat absoluteWidth;
@property(nonatomic) CGFloat absoluteHeight;

-(void)initializeSubView;

-(UIImage *)cropImage:(UIImage *)image;

-(CGPoint)correctPoint:(CGPoint )point;

@end
