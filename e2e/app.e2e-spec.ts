import { CSCD01Page } from './app.po';

describe('CSCD01 App', function() {
  let page: CSCD01Page;

  beforeEach(() => {
    page = new CSCD01Page();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
